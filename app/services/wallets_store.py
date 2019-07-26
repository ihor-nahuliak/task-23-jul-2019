from app.services.abstract_store import AbstractStore
from app.repos.wallets_repo import WalletsRepo


class WalletsStore(AbstractStore):
    repo_class = WalletsRepo
