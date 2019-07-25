from app.services.client_storage import ClientStorage
from app.services.transaction_storage import TransactionStorage


class BillingService:
    client_storage_class = ClientStorage
    transaction_storage_class = TransactionStorage

    async def send_money(self, transaction_id,
                         debit_wallet_id, credit_wallet_id,
                         payment_amount, payment_destination=''):
        """
        Debit wallet & credit wallet must have the same currency.
        If you wanna send money in credit currency,
        please buy needs amount in that currency first.

        :param transaction_id: must be asked to generate by frontend
        :param debit_wallet_id:
        :param credit_wallet_id:
        :param payment_amount:
        :param payment_destination:
        :return:
        """

        debit_wallet, credit_wallet = await self._get_wallets_pair(
            debit_wallet_id, credit_wallet_id)

        debit_payment = self._payment_storage.create_item(
            transaction_id=transaction_id,
            client_id=debit_wallet.client_id,
            wallet_id=debit_wallet.id,
            counterparty_client_id=credit_wallet.client_id,
            counterparty_wallet_id=credit_wallet.id,
            payment_currency=debit_wallet.currency,
            payment_amount=-1 * debit_amount,
            payment_destination=payment_destination,
        )

        credit_payment = self._payment_storage.create_item(
            transaction_id=transaction_id,
            client_id=credit_wallet.client_id,
            wallet_id=credit_wallet.id,
            counterparty_client_id=debit_wallet.client_id,
            counterparty_wallet_id=debit_wallet.id,
            payment_currency=credit_wallet.currency,
            payment_amount=+1 * credit_amount,
            payment_destination=payment_destination,
        )

    async def _get_wallets_pair(self, debit_wallet_id, credit_wallet_id):
        wallets = await self._wallet_storage.get_list(
            filter_params=bunch(id__in=[debit_wallet_id, credit_wallet_id]),
            slicing_params=bunch(limit=2)
        )
        wallets = {wallet.id: wallet for wallet in wallets}
        return wallets[debit_wallet_id], wallets[credit_wallet_id]
