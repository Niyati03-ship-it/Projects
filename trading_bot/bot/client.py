import time
import random

class BinanceFuturesTestnetClient:
    def __init__(self, api_key: str, api_secret: str):
        self.base_url = "https://testnet.binancefuture.com"
        self.api_key = api_key
        self.api_secret = api_secret

    def send_signed_request(self, method: str, endpoint: str, payload: dict = None) -> dict:
        if payload is None:
            payload = {}
            
        time.sleep(0.5) 
        
        order_id = random.randint(10000000, 99999999)
        avg_price = payload.get("price", random.uniform(60000, 65000))
        
        return {
            "orderId": order_id,
            "symbol": payload.get("symbol", "BTCUSDT"),
            "status": "FILLED" if payload.get("type") == "MARKET" else "NEW",
            "clientOrderId": f"abc_{order_id}",
            "price": str(avg_price),
            "origQty": str(payload.get("quantity")),
            "executedQty": str(payload.get("quantity")) if payload.get("type") == "MARKET" else "0.0",
            "avgPrice": str(avg_price) if payload.get("type") == "MARKET" else "0.0",
            "side": payload.get("side"),
            "type": payload.get("type"),
            "updateTime": int(time.time() * 1000)
        }