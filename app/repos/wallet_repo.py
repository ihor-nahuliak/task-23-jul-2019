from app.entities.wallet import Wallet


class WalletRepo:
    entity_class = Wallet

    def __init__(self, conn):
        self._conn = conn

    async def get_count(self, filter_params=None):
        pass

    async def get_list(self, filter_params=None, showing_params=None,
                       sorting_params=None, slicing_params=None):
        pass

    async def create_list(self, items_list):
        pass

    async def update_list(self, items_list):
        pass

    async def delete_list(self, filter_params=None):
        pass
