from dataclasses import dataclass
from datetime import datetime


@dataclass
class Wallet:
    id: int
    client_id: int
    currency: str
    is_enabled: bool = True
    created_at: datetime = datetime.now
    updated_at: datetime = None
    collected_balance: int = 0
    in_queue_balance: int = 0

    @property
    def balance(self):
        return self.collected_balance + self.in_queue_balance
