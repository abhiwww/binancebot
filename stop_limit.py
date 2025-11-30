import logging
from ..config import client
from ..utils import validate_symbol, validate_quantity, validate_price, handle_binance_error

logger = logging.getLogger(__name__)

def create_stop_limit_order(symbol, side, quantity, price, stop_price):
    """
    Create a stop-limit order
    
    Args:
        symbol (str): Trading pair
        side (str): 'BUY' or 'SELL'
        quantity (float): Order quantity
        price (float): Limit price
        stop_price (float): Stop price trigger
    
    Returns:
        dict: Order response
    """
    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        price = validate_price(price)
        stop_price = validate_price(stop_price)
        side = side.upper()
        
        if side not in ['BUY', 'SELL']:
            raise ValueError("Side must be 'BUY' or 'SELL'")
        
        logger.info(f"Placing stop-limit {side} order for {quantity} {symbol}, stop: ${stop_price}, limit: ${price}")
        
        # Place stop-limit order
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP',
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce='GTC'
        )
        
        logger.info(f"Stop-limit order placed: {order}")
        return order
        
    except Exception as e:
        error_msg = handle_binance_error(e, "stop-limit order")
        logger.error(f"Stop-limit order failed: {error_msg}")
        return {"error": error_msg}