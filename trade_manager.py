from models import Trade


class TradeManager:

    def __init__(self):
        self.trade = None

    def has_trade(self):
        return self.trade is not None

    def open_trade(self, trade: Trade):
        self.trade = trade

    def close_trade(
        self,
        exit_price,
        exit_time,
        status,
        profit_pips
    ):

        self.trade.exit_price = exit_price
        self.trade.exit_time = exit_time
        self.trade.status = status
        self.trade.profit_pips = profit_pips

        closed = self.trade

        self.trade = None

        return closed