class Performance:

    def __init__(self, starting_balance=1000):

        self.starting_balance = starting_balance


    def calculate_equity(self, trades):

        balance = self.starting_balance

        equity = []


        for trade in trades:

            balance += trade.profit_pips

            equity.append(balance)


        return equity



    def calculate_drawdown(self, equity):

        peak = equity[0]

        max_drawdown = 0


        for value in equity:

            if value > peak:
                peak = value


            drawdown = peak - value


            if drawdown > max_drawdown:
                max_drawdown = drawdown


        return max_drawdown