from config import (
    RSI_BUY_LEVEL,
    RSI_SELL_LEVEL,
    MIN_ATR,
    USE_RSI_FILTER,
    USE_MACD_FILTER,
    USE_ATR_FILTER,
)


def ema_strategy(df):
    """
    Enhanced EMA Strategy

    BUY:
        - EMA20 > EMA50
        - RSI > RSI_BUY_LEVEL
        - MACD > MACD_SIGNAL
        - ATR > MIN_ATR

    SELL:
        - EMA20 < EMA50
        - RSI < RSI_SELL_LEVEL
        - MACD < MACD_SIGNAL
        - ATR > MIN_ATR
    """

    if len(df) < 2:
        return "WAIT"

    current = df.iloc[-1]

    # ---------------- BUY ----------------

    buy = (
        current["EMA20"] > current["EMA50"]
    )

    if USE_RSI_FILTER:
        buy = buy and (
            current["RSI"] > RSI_BUY_LEVEL
        )

    if USE_MACD_FILTER:
        buy = buy and (
            current["MACD"] > current["MACD_SIGNAL"]
        )

    if USE_ATR_FILTER:
        buy = buy and (
            current["ATR"] > MIN_ATR
        )

    if buy:
        return "BUY"

    # ---------------- SELL ----------------

    sell = (
        current["EMA20"] < current["EMA50"]
    )

    if USE_RSI_FILTER:
        sell = sell and (
            current["RSI"] < RSI_SELL_LEVEL
        )

    if USE_MACD_FILTER:
        sell = sell and (
            current["MACD"] < current["MACD_SIGNAL"]
        )

    if USE_ATR_FILTER:
        sell = sell and (
            current["ATR"] > MIN_ATR
        )

    if sell:
        return "SELL"

    return "WAIT"