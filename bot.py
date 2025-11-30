#!/usr/bin/env python3
import argparse
import sys
import logging
from .market_orders import create_market_order
from .limit_orders import create_limit_order
from .advanced.stop_limit import create_stop_limit_order
from .utils import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Market order parser
    market_parser = subparsers.add_parser('market', help='Place market order')
    market_parser.add_argument('symbol', help='Trading symbol (e.g., BTCUSDT)')
    market_parser.add_argument('side', choices=['BUY', 'SELL'], help='Order side')
    market_parser.add_argument('quantity', type=float, help='Order quantity')
    
    # Limit order parser
    limit_parser = subparsers.add_parser('limit', help='Place limit order')
    limit_parser.add_argument('symbol', help='Trading symbol (e.g., BTCUSDT)')
    limit_parser.add_argument('side', choices=['BUY', 'SELL'], help='Order side')
    limit_parser.add_argument('quantity', type=float, help='Order quantity')
    limit_parser.add_argument('price', type=float, help='Limit price')
    
    # Stop-limit order parser
    stop_limit_parser = subparsers.add_parser('stop-limit', help='Place stop-limit order')
    stop_limit_parser.add_argument('symbol', help='Trading symbol')
    stop_limit_parser.add_argument('side', choices=['BUY', 'SELL'], help='Order side')
    stop_limit_parser.add_argument('quantity', type=float, help='Order quantity')
    stop_limit_parser.add_argument('price', type=float, help='Limit price')
    stop_limit_parser.add_argument('stop_price', type=float, help='Stop price')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == 'market':
            result = create_market_order(args.symbol, args.side, args.quantity)
        elif args.command == 'limit':
            result = create_limit_order(args.symbol, args.side, args.quantity, args.price)
        elif args.command == 'stop-limit':
            result = create_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
        else:
            print(f"Unknown command: {args.command}")
            sys.exit(1)
        
        if 'error' in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        else:
            print(f"Order successful: {result}")
            
    except Exception as e:
        logger.error(f"CLI execution failed: {str(e)}")
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()