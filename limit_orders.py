import logging
from .config import client
from .utils import validate_symbol, validate_quantity, validate_price, handle_binance_error

logger = logging.getLogger(__name__)

def create_limit_order(symbol, side, quantity, price, timeInForce='GTC'):
    """
    Create a limit order
    
    Args:
        symbol (str): Trading pair (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Order quantity
        price (float): Limit price
        timeInForce (str): Order time in force (default: 'GTC')
    
    Returns:
        dict: Order response
    """
    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        price = validate_price(price)
        side = side.upper()
        
        if side not in ['BUY', 'SELL']:
            raise ValueError("Side must be 'BUY' or 'SELL'")
        
        logger.info(f"Placing limit {side} order for {quantity} {symbol} at ${price}")
        
        # Place limit order
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce=timeInForce
        )
        
        logger.info(f"Limit order placed: {order}")
        return order
        
    except Exception as e:
        error_msg = handle_binance_error(e, "limit order")
        logger.error(f"Limit order failed: {error_msg}")
        return {"error": error_msg}