from datetime import datetime as dt

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as sa_psql

from app.tables.meta import metadata
from app.tables.tbl_clients import tbl_clients
from app.tables.tbl_wallets import tbl_wallets


tbl_payments = sa.Table(
    'billing__payments', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('is_enabled', sa.Boolean(), default=True, index=True),
    sa.Column('created_at', sa.DateTime(), default=dt.utcnow, index=True),
    sa.Column('updated_at', sa.DateTime(), onupdate=dt.utcnow, index=True),
    sa.Column('transaction_id', sa_psql.UUID(), index=True),
    sa.Column('transaction_type', sa.String(length=16), index=True),
    sa.Column('transaction_status', sa.String(length=16), index=True),
    sa.Column('client_id',
              sa.ForeignKey(tbl_clients.c.id, ondelete='NO ACTION')),
    sa.Column('wallet_id',
              sa.ForeignKey(tbl_wallets.c.id, ondelete='NO ACTION')),
    sa.Column('currency', sa.String(length=3), index=True,
              comment='billing__wallets.currency: iso-4217 string code'),
    sa.Column('amount', sa.Integer(), index=True,
              comment='in cents, is negative for debit payments. '
                      'Payment is debit when client_id pays money. '
                      'Payment is credit when client_id takes money.'),
    sa.Column('partner_client_id', sa.Integer(), index=True),
    sa.Column('partner_wallet_id', sa.Integer(), index=True),
    sa.Column('partner_currency', sa.String(length=3), index=True),
    sa.Column('partner_amount', sa.Integer(), index=True,
              comment='in cents, is negative for credit payments. '
                      'Payment is debit when client_id pays money. '
                      'Payment is credit when client_id takes money.'),
    sa.Column('exchange_rate', sa.DECIMAL(), nullable=True),

    # as we don't so complex operations,
    # we can require unique payment per wallet
    sa.UniqueConstraint('transaction_id', 'wallet_id',
                        name='unq__payments__transaction_id_wallet_id'),
)
