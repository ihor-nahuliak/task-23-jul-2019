import uuid

import marshmallow as ma

from app.serializers import validators as vld
from app.utils import iso_datetime


class ClientSchema(ma.Schema):
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
    name = ma.fields.String(
        required=True, allow_none=True, missing=None,
        validate=vld.client_name_validator)
    country = ma.fields.String(
        required=True, allow_none=True, missing=None,
        validate=vld.country_name_validator)
    city = ma.fields.String(
        required=True, allow_none=True, missing=None,
        validate=vld.city_name_validator)
