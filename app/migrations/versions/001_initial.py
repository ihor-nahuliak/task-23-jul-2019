from datetime import datetime as dt

from migrate import *
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as sa_psql


metadata = sa.MetaData()


tbl_clients = sa.Table(
    'billing__clients', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('is_enabled', sa.Boolean(), default=True, index=True),
    sa.Column('created_at', sa.DateTime(), default=dt.utcnow, index=True),
    sa.Column('updated_at', sa.DateTime(), onupdate=dt.utcnow, index=True),
    sa.Column('name', sa.String(length=160), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
)

tbl_wallets = sa.Table(
    'billing__wallets', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('is_enabled', sa.Boolean(), default=True, index=True),
    sa.Column('created_at', sa.DateTime(), default=dt.utcnow, index=True),
    sa.Column('updated_at', sa.DateTime(), onupdate=dt.utcnow, index=True),
    sa.Column('client_id',
              sa.ForeignKey(tbl_clients.c.id, ondelete='CASCADE')),
    sa.Column('currency', sa.String(length=3), index=True,
              comment='iso-4217 string code'),
    sa.Column('collected_balance', sa.Integer(), default=0,
              comment='Collected wallet balance part, in cents. '
                      'To take the real wallet balance add the '
                      'sum of all "accepted" payments amounts.'),

    # the task requirement is: "one wallet per client",
    # but we dilate it to: "each client has just one wallet per currency"
    sa.UniqueConstraint('client_id', 'currency',
                        name='unq__wallets__client_id_currency'),
)

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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    tbl_clients.create()
    tbl_wallets.create()
    tbl_payments.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    tbl_payments.drop()
    tbl_wallets.drop()
    tbl_clients.drop()
