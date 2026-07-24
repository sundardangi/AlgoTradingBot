import ta

def calculate_ema(df):
    """
    Calculate EMA20 and EMA50
    """

    df["EMA20"] = ta.trend.ema_indicator(
        df["close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        df["close"],
        window=50
    )

    return df