import pandas as pd

from indicators import calculate_ema
from strategy import ema_strategy
from models import Trade
from config import STOP_LOSS_PIPS, TAKE_PROFIT_PIPS


class Backtester:

    def check_buy_exit(self, trade, future_candles):

        for _, candle in future_candles.iterrows():

            if candle["low"] <= trade.stop_loss:
                return "LOSS"

            if candle["high"] >= trade.take_profit:
                return "WIN"

        return "OPEN"


    def check_sell_exit(self, trade, future_candles):

        for _, candle in future_candles.iterrows():

            if candle["high"] >= trade.stop_loss:
                return "LOSS"

            if candle["low"] <= trade.take_profit:
                return "WIN"

        return "OPEN"


    def run(self, filename):

        df = pd.read_csv(filename)

        df["time"] = pd.to_datetime(df["time"])

        df = calculate_ema(df)

        trades = []

        pip = 0.0001


        for i in range(50, len(df)):

            signal = ema_strategy(df.iloc[:i + 1])

            price = df.iloc[i]["close"]


            if signal == "BUY":

                trade = Trade(
                    direction="BUY",
                    entry_time=df.iloc[i]["time"],
                    entry_price=price,
                    stop_loss=price - (STOP_LOSS_PIPS * pip),
                    take_profit=price + (TAKE_PROFIT_PIPS * pip)
                )

                future = df.iloc[i + 1:]

                trade.status = self.check_buy_exit(trade, future)


                if trade.status == "WIN":
                    trade.profit_pips = TAKE_PROFIT_PIPS

                elif trade.status == "LOSS":
                    trade.profit_pips = -STOP_LOSS_PIPS


                trades.append(trade)


            elif signal == "SELL":

                trade = Trade(
                    direction="SELL",
                    entry_time=df.iloc[i]["time"],
                    entry_price=price,
                    stop_loss=price + (STOP_LOSS_PIPS * pip),
                    take_profit=price - (TAKE_PROFIT_PIPS * pip)
                )

                future = df.iloc[i + 1:]

                trade.status = self.check_sell_exit(trade, future)


                if trade.status == "WIN":
                    trade.profit_pips = TAKE_PROFIT_PIPS

                elif trade.status == "LOSS":
                    trade.profit_pips = -STOP_LOSS_PIPS


                trades.append(trade)



        wins = sum(1 for t in trades if t.status == "WIN")

        losses = sum(1 for t in trades if t.status == "LOSS")

        open_trades = sum(1 for t in trades if t.status == "OPEN")


        total = len(trades)


        win_rate = (
            (wins / total) * 100
            if total > 0
            else 0
        )


        total_pips = sum(t.profit_pips for t in trades)


        winning_pips = [
            t.profit_pips
            for t in trades
            if t.profit_pips > 0
        ]


        losing_pips = [
            t.profit_pips
            for t in trades
            if t.profit_pips < 0
        ]


        avg_win = (
            sum(winning_pips) / len(winning_pips)
            if winning_pips
            else 0
        )


        avg_loss = (
            sum(losing_pips) / len(losing_pips)
            if losing_pips
            else 0
        )


        gross_profit = sum(winning_pips)

        gross_loss = abs(sum(losing_pips))


        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else 0
        )


        print("\n========== BACKTEST REPORT ==========")

        print(f"Total Trades  : {total}")
        print(f"Wins          : {wins}")
        print(f"Losses        : {losses}")
        print(f"Open          : {open_trades}")

        print()

        print(f"Win Rate      : {win_rate:.2f}%")
        print(f"Total Pips    : {total_pips}")
        print(f"Avg Win       : {avg_win:.2f}")
        print(f"Avg Loss      : {avg_loss:.2f}")
        print(f"Profit Factor : {profit_factor:.2f}")

        print("====================================")