from datetime import datetime as dt

import sqlalchemy as sa
from migrate import *


metadata = sa.MetaData()


tbl_clients = sa.Table(
    'billing__clients', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('created_at', sa.DateTime(), default=dt.utcnow, index=True),
    sa.Column('updated_at', sa.DateTime(), onupdate=dt.utcnow, index=True),
    sa.Column('name', sa.String(length=160), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    tbl_clients.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    tbl_clients.drop()
