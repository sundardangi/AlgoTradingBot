from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:
    direction: str

    entry_time: datetime
    entry_price: float

    stop_loss: float
    take_profit: float

    exit_time: datetime | None = None
    exit_price: float | None = None

    profit_pips: float = 0.0
    profit_money: float = 0.0

    bars_held: int = 0

    risk_reward: float = 0.0

    status: str = "OPEN"