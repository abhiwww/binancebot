import logging
from decimal import Decimal, InvalidOperation
from binance.exceptions import BinanceAPIException

def setup_logging():
    """Setup structured logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('bot.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def validate_symbol(symbol):
    """Validate trading symbol"""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    return symbol.upper()

def validate_quantity(quantity):
    """Validate quantity"""
    try:
        qty = Decimal(str(quantity))
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        return float(qty)
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid quantity format")

def validate_price(price):
    """Validate price"""
    try:
        price_val = Decimal(str(price))
        if price_val <= 0:
            raise ValueError("Price must be positive")
        return float(price_val)
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid price format")

def handle_binance_error(error, operation):
    """Handle Binance API errors"""
    logger = logging.getLogger(__name__)
    if isinstance(error, BinanceAPIException):
        logger.error(f"Binance API error during {operation}: {error.message}")
        return f"API Error: {error.message}"
    else:
        logger.error(f"Unexpected error during {operation}: {str(error)}")
        return f"Unexpected error: {str(error)}"