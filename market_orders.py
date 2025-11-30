import logging
from .config import client
from .utils import validate_symbol, validate_quantity, handle_binance_error

logger = logging.getLogger(__name__)

def create_market_order(symbol, side, quantity):
    """
    Create a market order
    
    Args:
        symbol (str): Trading pair (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Order quantity
    
    Returns:
        dict: Order response
    """
    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)
        side = side.upper()
        
        if side not in ['BUY', 'SELL']:
            raise ValueError("Side must be 'BUY' or 'SELL'")
        
        logger.info(f"Placing market {side} order for {quantity} {symbol}")
        
        # Place market order
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        
        logger.info(f"Market order executed: {order}")
        return order
        
    except Exception as e:
        error_msg = handle_binance_error(e, "market order")
        logger.error(f"Market order failed: {error_msg}")
        return {"error": error_msg}