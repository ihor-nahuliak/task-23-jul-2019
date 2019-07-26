from datetime import datetime as dt

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as sa_psql

from app.tables.meta import metadata


tbl_clients = sa.Table(
    'billing__clients', metadata,

    sa.Column('id', sa_psql.UUID(), primary_key=True),
    sa.Column('is_enabled', sa.Boolean(), default=True, index=True),
    sa.Column('created_at', sa.DateTime(), default=dt.utcnow, index=True),
    sa.Column('updated_at', sa.DateTime(), onupdate=dt.utcnow, index=True),
    sa.Column('name', sa.String(length=160), nullable=True),
    sa.Column('country', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=80), nullable=True),
)
