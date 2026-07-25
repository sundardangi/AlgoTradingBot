class Performance:

    def __init__(self, starting_balance=1000):
        self.starting_balance = starting_balance

    def calculate_equity(self, trades):

        balance = self.starting_balance
        equity = []

        for trade in trades:

            # Ignore trades still open
            if trade.status == "OPEN":
                equity.append(balance)
                continue

            balance += trade.profit_pips

            equity.append(balance)

        return equity

    def calculate_drawdown(self, equity):

        if not equity:
            return 0

        peak = equity[0]
        max_drawdown = 0

        for value in equity:

            if value > peak:
                peak = value

            drawdown = peak - value

            if drawdown > max_drawdown:
                max_drawdown = drawdown

        return max_drawdown

    def win_rate(self, trades):

        closed = [t for t in trades if t.status != "OPEN"]

        if not closed:
            return 0

        wins = sum(1 for t in closed if t.status == "WIN")

        return (wins / len(closed)) * 100

    def profit_factor(self, trades):

        gross_profit = sum(
            t.profit_pips
            for t in trades
            if t.profit_pips > 0
        )

        gross_loss = abs(
            sum(
                t.profit_pips
                for t in trades
                if t.profit_pips < 0
            )
        )

        if gross_loss == 0:
            return 0

        return gross_profit / gross_loss