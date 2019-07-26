import uuid

import marshmallow as ma

from app.serializers import validators as vld
from app.utils import iso_datetime


class WalletSchema(ma.Schema):
    id = ma.fields.UUID(
        required=True, missing=uuid.uuid4)
    is_enabled = ma.fields.Boolean(
        required=True, missing=True)
    created_at = ma.fields.DateTime(
        required=True, missing=iso_datetime,
        format=vld.datetime_iso_format)
    updated_at = ma.fields.DateTime(
        required=True, allow_none=True, missing=iso_datetime,
        format=vld.datetime_iso_format)
    client_id = ma.fields.UUID(
        required=True)
    currency = ma.fields.String(
        required=True, validate=vld.currency_validator)
