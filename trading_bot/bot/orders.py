import logging

logger = logging.getLogger("TradingBot.Orders")

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_futures_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        endpoint = "/fapi/v1/order"
        
        payload = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }
        
        if order_type.upper() == "LIMIT":
            payload["price"] = price
            payload["timeInForce"] = "GTC"  

        logger.info(f"Sending Order Request: {payload}")
        
        try:
            response = self.client.send_signed_request("POST", endpoint, payload)
            logger.info(f"Order Executed Successfully. Response: {response}")
            return response
        except Exception as e:
            logger.error(f"Failed to place order. Error: {str(e)}")
            raise e