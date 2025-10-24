import sys
import logging
from datetime import datetime

# ----------------- Logging Setup -----------------
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# ----------------- Mock Bot Class -----------------
class MockTradingBot:
    def __init__(self):
        logging.info("Initialized Mock Trading Bot.")

    def place_market_order(self, symbol, side, quantity):
        """Simulate a market order (BUY/SELL)."""
        order = {
            'symbol': symbol,
            'side': side,
            'type': 'MARKET',
            'quantity': quantity,
            'timestamp': str(datetime.now())
        }
        logging.info(f"[SIMULATED] Market Order: {order}")
        print(f"⚙️ Running in MOCK MODE")
        print(f"🧪 [SIMULATED ORDER] {order}")
        print(f"✅ Market order executed for {symbol} ({side}, {quantity})")

    def place_limit_order(self, symbol, side, quantity, price):
        """Simulate a limit order (BUY/SELL)."""
        order = {
            'symbol': symbol,
            'side': side,
            'type': 'LIMIT',
            'quantity': quantity,
            'price': price,
            'timestamp': str(datetime.now())
        }
        logging.info(f"[SIMULATED] Limit Order: {order}")
        print(f"⚙️ Running in MOCK MODE")
        print(f"🧪 [SIMULATED ORDER] {order}")
        print(f"✅ Limit order placed for {symbol} ({side}, {quantity} @ {price})")

# ----------------- Command-Line Interface -----------------
def main():
    """
    Usage:
    Market order:
        python mock_trading_bot.py SYMBOL SIDE MARKET QUANTITY
    Limit order:
        python mock_trading_bot.py SYMBOL SIDE LIMIT QUANTITY PRICE
    Example:
        python mock_trading_bot.py BTCUSDT BUY MARKET 0.01
        python mock_trading_bot.py BTCUSDT SELL LIMIT 0.01 30000
    """
    if len(sys.argv) < 5:
        print(main.__doc__)
        sys.exit(1)

    symbol = sys.argv[1].upper()
    side = sys.argv[2].upper()
    order_type = sys.argv[3].upper()
    quantity = float(sys.argv[4])
    price = float(sys.argv[5]) if order_type == "LIMIT" and len(sys.argv) == 6 else None

    bot = MockTradingBot()

    if order_type == "MARKET":
        bot.place_market_order(symbol, side, quantity)
    elif order_type == "LIMIT" and price is not None:
        bot.place_limit_order(symbol, side, quantity, price)
    else:
        print("❌ Invalid order type or missing price for LIMIT order.")
        sys.exit(1)

if __name__ == "__main__":
    main()
