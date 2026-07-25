import pandas as pd

from indicators import calculate_ema
from strategy import ema_strategy
from models import Trade
from config import STOP_LOSS_PIPS, TAKE_PROFIT_PIPS
from performance import Performance
from chart import Chart


MAX_HOLD_CANDLES = 50


class Backtester:


    def check_buy_exit(self, trade, future_candles):

        for _, candle in future_candles.iterrows():

            # Both SL and TP hit in same candle
            if (
                candle["low"] <= trade.stop_loss
                and
                candle["high"] >= trade.take_profit
            ):
                return "LOSS"


            if candle["low"] <= trade.stop_loss:
                return "LOSS"


            if candle["high"] >= trade.take_profit:
                return "WIN"


        return "OPEN"



    def check_sell_exit(self, trade, future_candles):

        for _, candle in future_candles.iterrows():


            # Both SL and TP hit
            if (
                candle["high"] >= trade.stop_loss
                and
                candle["low"] <= trade.take_profit
            ):
                return "LOSS"


            if candle["high"] >= trade.stop_loss:
                return "LOSS"


            if candle["low"] <= trade.take_profit:
                return "WIN"


        return "OPEN"



    def run(self, filename):


        df = pd.read_csv(filename)


        df["time"] = pd.to_datetime(
            df["time"]
        )


        df = calculate_ema(df)



        trades = []


        pip = 0.0001






        for i in range(50, len(df)):




            signal = ema_strategy(
                df.iloc[:i+1]
            )


            price = df.iloc[i]["close"]



            # ================= BUY =================

            if signal == "BUY":


                trade = Trade(

                    direction="BUY",

                    entry_time=df.iloc[i]["time"],

                    entry_price=price,

                    stop_loss=(
                        price -
                        STOP_LOSS_PIPS * pip
                    ),

                    take_profit=(
                        price +
                        TAKE_PROFIT_PIPS * pip
                    )
                )



                future = df.iloc[
                    i+1:
                    i+1+MAX_HOLD_CANDLES
                ]



                trade.status = self.check_buy_exit(
                    trade,
                    future
                )



                if trade.status == "WIN":

                    trade.profit_pips = TAKE_PROFIT_PIPS



                elif trade.status == "LOSS":

                    trade.profit_pips = -STOP_LOSS_PIPS



                else:

                    trade.profit_pips = 0



                trades.append(trade)




            # ================= SELL =================


            elif signal == "SELL":



                trade = Trade(

                    direction="SELL",

                    entry_time=df.iloc[i]["time"],

                    entry_price=price,


                    stop_loss=(
                        price +
                        STOP_LOSS_PIPS * pip
                    ),


                    take_profit=(
                        price -
                        TAKE_PROFIT_PIPS * pip
                    )

                )



                future = df.iloc[
                    i+1:
                    i+1+MAX_HOLD_CANDLES
                ]



                trade.status = self.check_sell_exit(
                    trade,
                    future
                )



                if trade.status == "WIN":

                    trade.profit_pips = TAKE_PROFIT_PIPS



                elif trade.status == "LOSS":

                    trade.profit_pips = -STOP_LOSS_PIPS



                else:

                    trade.profit_pips = 0



                trades.append(trade)


                active_trade = True



        # ================= REPORT =================


        wins = sum(
            1 for t in trades
            if t.status == "WIN"
        )


        losses = sum(
            1 for t in trades
            if t.status == "LOSS"
        )


        opens = sum(
            1 for t in trades
            if t.status == "OPEN"
        )


        total = len(trades)



        win_rate = (

            wins / total * 100

            if total > 0

            else 0

        )



        total_pips = sum(
            t.profit_pips
            for t in trades
        )



        winning = [

            t.profit_pips

            for t in trades

            if t.profit_pips > 0

        ]



        losing = [

            t.profit_pips

            for t in trades

            if t.profit_pips < 0

        ]



        avg_win = (

            sum(winning)/len(winning)

            if winning

            else 0

        )



        avg_loss = (

            sum(losing)/len(losing)

            if losing

            else 0

        )



        gross_profit = sum(winning)


        gross_loss = abs(sum(losing))



        profit_factor = (

            gross_profit/gross_loss

            if gross_loss > 0

            else 0

        )



        performance = Performance(1000)



        equity = performance.calculate_equity(
            trades
        )


        max_drawdown = performance.calculate_drawdown(
            equity
        )



        if equity:

            chart = Chart()

            chart.plot_equity(
                equity
            )



        print("\n========== BACKTEST REPORT ==========")

        print(f"Total Trades  : {total}")

        print(f"Wins          : {wins}")

        print(f"Losses        : {losses}")

        print(f"Open          : {opens}")

        print()

        print(f"Win Rate      : {win_rate:.2f}%")

        print(f"Total Pips    : {total_pips}")

        print(f"Avg Win       : {avg_win:.2f}")

        print(f"Avg Loss      : {avg_loss:.2f}")

        print(f"Profit Factor : {profit_factor:.2f}")

        print()

        print("Starting Balance : $1000")


        if equity:

            print(
                f"Ending Balance   : ${equity[-1]:.2f}"
            )


        print(
            f"Max Drawdown     : ${max_drawdown:.2f}"
        )

        print("====================================")





# ================= RUN BOT =================


# ================= RUN BOT =================

if __name__ == "__main__":

    tester = Backtester()

    tester.run(
        "data/history.csv"
    )