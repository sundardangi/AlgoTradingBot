import matplotlib.pyplot as plt


class Chart:

    def plot_equity(self, equity):

        plt.figure(figsize=(10,5))

        plt.plot(equity)

        plt.title("Equity Curve")

        plt.xlabel("Trade Number")

        plt.ylabel("Balance ($)")

        plt.grid(True)

        plt.show()