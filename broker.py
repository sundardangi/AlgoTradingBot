import MetaTrader5 as mt5
import pandas as pd


class Broker:

    def connect(self):
        if not mt5.initialize():
            raise Exception("Failed to connect to MT5")

        print("✅ Connected to MT5")

    def disconnect(self):
        mt5.shutdown()

    def get_balance(self):
        account = mt5.account_info()
        return account.balance

    def get_candles(self, symbol, timeframe, count):
        rates = mt5.copy_rates_from_pos(
            symbol,
            timeframe,
            0,
            count
        )

        if rates is None:
            raise Exception("Failed to retrieve candle data.")

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s")

        return df

    def get_tick(self, symbol):
        tick = mt5.symbol_info_tick(symbol)

        if tick is None:
            raise Exception("Failed to retrieve tick data.")

        return tick

    def save_candles(self, symbol, timeframe, count, filename):
        candles = self.get_candles(symbol, timeframe, count)

        candles.to_csv(filename, index=False)

        print(f"✅ Saved {len(candles)} candles to {filename}")