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
    profit: float = 0.0
    status: str = "OPEN"