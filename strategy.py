def ema_strategy(df):

    previous = df.iloc[-2]
    current = df.iloc[-1]

    # BUY crossover
    if (
        previous["EMA20"] < previous["EMA50"]
        and
        current["EMA20"] > current["EMA50"]
    ):
        return "BUY"

    # SELL crossover
    if (
        previous["EMA20"] > previous["EMA50"]
        and
        current["EMA20"] < current["EMA50"]
    ):
        return "SELL"

    return "WAIT"