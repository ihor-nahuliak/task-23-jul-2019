import gzip
import ujson as json
from aiohttp import web


class JsonResponse(web.Response):
    """It uses faster ujson."""

    def __init__(self, data, status=200, headers=None,
                 compress=False, content_type='application/json'):
        data = bytes(json.dumps(data), 'utf-8')
        headers = headers or {}

        if compress:
            data = gzip.compress(data, compresslevel=5)
            headers['Content-Encoding'] = 'gzip'

        super(JsonResponse, self).__init__(
            body=data, status=status, headers=headers,
            content_type=content_type)
