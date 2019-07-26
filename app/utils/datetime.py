from datetime import datetime
from marshmallow.utils import isoformat


def iso_datetime():
    return isoformat(datetime.utcnow().replace(microsecond=0))
