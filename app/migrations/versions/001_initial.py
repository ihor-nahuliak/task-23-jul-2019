from datetime import datetime as dt

import sqlalchemy as sa
from migrate import *


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
    sa.Column('client_id', sa.ForeignKey(tbl_clients.c.id,
                                         ondelete='CASCADE')),
    sa.Column('currency', sa.String(length=3), index=True,
              comment='iso-4217 string code'),
    sa.Column('collected_balance', sa.Integer(), default=0,
              comment='Collected wallet balance part, in cents. '
                      'To take the real wallet balance add the '
                      'sum of all "accepted" payments amounts.')
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    tbl_clients.create()
    tbl_wallets.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    tbl_wallets.drop()
    tbl_clients.drop()
