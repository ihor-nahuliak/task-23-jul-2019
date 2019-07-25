import unittest
import unittest.mock as mock

import gzip

from app.utils.json_response import JsonResponse


class TestCase(unittest.TestCase):

    @mock.patch('aiohttp.web.Response.__init__')
    def test_default_params_call_dict(self, m_aiohttp_response_class_init):
        JsonResponse({})

        m_aiohttp_response_class_init.assert_called_once_with(
            body=b'{}',
            status=200,
            headers={},
            content_type='application/json')

    @mock.patch('aiohttp.web.Response.__init__')
    def test_default_params_call_list(self, m_aiohttp_response_class_init):
        JsonResponse([])

        m_aiohttp_response_class_init.assert_called_once_with(
            body=b'[]',
            status=200,
            headers={},
            content_type='application/json')

    @mock.patch('aiohttp.web.Response.__init__')
    def test_call_custom_status(self, m_aiohttp_response_class_init):
        JsonResponse({'error': 'validation_error'}, status=400)

        m_aiohttp_response_class_init.assert_called_once_with(
            body=b'{"error":"validation_error"}',
            status=400,
            headers={},
            content_type='application/json')

    @mock.patch('aiohttp.web.Response.__init__')
    def test_call_custom_content_type(self, m_aiohttp_response_class_init):
        JsonResponse({'abc': '123'}, content_type='text/x-json; charset=utf-8')

        m_aiohttp_response_class_init.assert_called_once_with(
            body=b'{"abc":"123"}',
            status=200,
            headers={},
            content_type='text/x-json; charset=utf-8')

    @mock.patch('aiohttp.web.Response.__init__')
    def test_call_compress(self, m_aiohttp_response_class_init):
        JsonResponse({}, compress=True)

        m_aiohttp_response_class_init.assert_called_once_with(
            body=gzip.compress(b'{}', compresslevel=5),
            status=200,
            headers={'Content-Encoding': 'gzip'},
            content_type='application/json')

    @mock.patch('aiohttp.web.Response.__init__')
    def test_call_compress_with_headers(self, m_aiohttp_response_class_init):
        JsonResponse({}, headers={'My-Header': 'test'}, compress=True)

        m_aiohttp_response_class_init.assert_called_once_with(
            body=gzip.compress(b'{}', compresslevel=5),
            status=200,
            headers={'My-Header': 'test', 'Content-Encoding': 'gzip'},
            content_type='application/json')
