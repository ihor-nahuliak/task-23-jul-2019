from datetime import datetime as dt

import sqlalchemy as sa

from app.tables.meta import metadata
from app.tables.tbl_clients import tbl_clients


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
