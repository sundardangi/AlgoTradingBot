import ta


def calculate_ema(df):
    """
    Calculate technical indicators
    EMA20, EMA50, RSI, ATR
    """

    # EMA indicators
    df["EMA20"] = ta.trend.ema_indicator(
        df["close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        df["close"],
        window=50
    )


    # RSI indicator
    df["RSI"] = ta.momentum.rsi(
        df["close"],
        window=14
    )


    # ATR volatility indicator
    df["ATR"] = ta.volatility.average_true_range(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )


    # Remove incomplete rows
    df.dropna(inplace=True)


    return df