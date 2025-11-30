import os
from decimal import Decimal
from binance.client import Client

# Binance API Configuration
API_KEY = os.getenv('BINANCE_API_KEY', 'your_api_key_here')
API_SECRET = os.getenv('BINANCE_API_SECRET', 'your_api_secret_here')

# Initialize Binance Client
client = Client(API_KEY, API_SECRET, testnet=True)  # Use testnet for development

# Trading Configuration
MAX_LEVERAGE = 10
DEFAULT_LEVERAGE = 3