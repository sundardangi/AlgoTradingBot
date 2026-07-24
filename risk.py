def calculate_risk(balance, risk_percent):
    """
    Calculate the maximum amount to risk on one trade.
    """

    risk_amount = balance * (risk_percent / 100)

    return risk_amount