from marshmallow import validate as vld


datetime_iso_format = '%Y-%m-%dT%H:%M:%S+00:00'

client_name_validator = vld.Length(min=1, max=160)

country_name_validator = vld.Length(min=1, max=40)

city_name_validator = vld.Length(min=1, max=80)

currency_validator = vld.OneOf(['USD', 'EUR', 'CAD', 'CNY'])
