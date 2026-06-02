import os
import sys
import argparse
from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.client import BinanceFuturesTestnetClient
from bot.orders import OrderManager

def main():
    logger = setup_logging()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Simplified Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")
    
    args = parser.parse_args()

    
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("Environment variables BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET must be set.")
        print("\n[ERROR] Missing API Credentials. Please export your keys first.")
        sys.exit(1)


    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
    except ValueError as val_err:
        logger.error(f"Validation Error: {str(val_err)}")
        print(f"\n[INPUT ERROR] {val_err}")
        sys.exit(1)

    try:
        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol.upper()} | Side: {args.side.upper()} | Type: {args.type.upper()} | Qty: {args.quantity} | Price: {args.price}")
        
        client = BinanceFuturesTestnetClient(api_key, api_secret)
        manager = OrderManager(client)
        
        response = manager.place_futures_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        print("\n--- Order Response Details ---")
        print(f"Status: SUCCESS")
        print(f"OrderID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')} USDT")
        
    except Exception as api_err:
        print(f"\n[API/NETWORK ERROR] Execution Failed. Check 'bot.log' for details.")
        print(f"Details: {api_err}")

if __name__ == "__main__":
    main()