import ta


def calculate_ema(df):
    """
    Calculate technical indicators:
    - EMA20
    - EMA50
    - RSI 14
    - ATR 14
    """

    # Make sure data is sorted correctly
    df = df.sort_values("time").copy()


    # ================= EMA =================

    df["EMA20"] = ta.trend.ema_indicator(
        close=df["close"],
        window=20
    )


    df["EMA50"] = ta.trend.ema_indicator(
        close=df["close"],
        window=50
    )



    # ================= RSI =================

    df["RSI"] = ta.momentum.rsi(
        close=df["close"],
        window=14
    )



    # ================= ATR =================

    df["ATR"] = ta.volatility.average_true_range(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )



    # ================= MACD =================
    # Helps detect momentum

    df["MACD"] = ta.trend.macd(
        close=df["close"]
    )


    df["MACD_SIGNAL"] = ta.trend.macd_signal(
        close=df["close"]
    )



    # Remove incomplete indicator rows

    df.dropna(
        inplace=True
    )


    return df