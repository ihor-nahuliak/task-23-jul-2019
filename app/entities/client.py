from dataclasses import dataclass
from typing import List
from datetime import datetime

from .wallet import Wallet


@dataclass
class Client:
    id: int
    is_enabled: bool = True
    created_at: datetime = datetime.now
    updated_at: datetime = None
    name: str = None
    country: str = None
    city: str = None
    wallets_list: List[Wallet] = list
