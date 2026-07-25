"""
=====================================================
AlgoTradingBot V2 Configuration
=====================================================
"""

# ==========================
# MARKET
# ==========================

SYMBOL = "EURUSDm"
TIMEFRAME = "M5"

# ==========================
# ACCOUNT
# ==========================

STARTING_BALANCE = 1000.0
RISK_PERCENT = 1.0

# ==========================
# STRATEGY
# ==========================

EMA_FAST = 20
EMA_SLOW = 50

RSI_PERIOD = 14
RSI_BUY_LEVEL = 55
RSI_SELL_LEVEL = 45

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

ATR_PERIOD = 14

# ==========================
# RISK MANAGEMENT
# ==========================

USE_ATR_STOP = True

ATR_STOP_MULTIPLIER = 1.5
ATR_TAKE_PROFIT_MULTIPLIER = 3.0

STOP_LOSS_PIPS = 20
TAKE_PROFIT_PIPS = 40

MAX_HOLD_CANDLES = 50

# ==========================
# TRADING COSTS
# ==========================

SPREAD_PIPS = 1.0
COMMISSION_PER_LOT = 0.0
SLIPPAGE_PIPS = 0.5

# ==========================
# FILTERS
# ==========================

USE_RSI_FILTER = True
USE_MACD_FILTER = True
USE_ATR_FILTER = True

MIN_ATR = 0.00030

# ==========================
# REPORTING
# ==========================

EXPORT_TRADES = True
SAVE_EQUITY_CURVE = True

# ==========================
# MAGIC NUMBER
# ==========================

MAGIC_NUMBER = 10001