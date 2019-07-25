import asynctest as unittest

from aiohttp.test_utils import AioHTTPTestCase as _TestCase
from aiohttp.test_utils import unittest_run_loop

from app.application import create_app


class TestCase(_TestCase):

    async def get_application(self):
        return await create_app()

    @unittest_run_loop
    async def test_index_html_url_returns_200(self):
        resp = await self.client.request('GET', '/index.html')

        self.assertEqual(resp.status, 200)

    @unittest_run_loop
    async def test_root_url_returns_200(self):
        resp = await self.client.request('GET', '/')

        self.assertEqual(resp.status, 200)

    @unittest_run_loop
    async def test_index_page_returns_html_content_type(self):
        resp = await self.client.request('GET', '/')

        self.assertEqual(resp.content_type, 'text/html')

    @unittest_run_loop
    async def test_index_page_returns_html(self):
        resp = await self.client.request('GET', '/')
        resp_html = await resp.text()

        self.assertTrue(resp_html.startswith('<!DOCTYPE html>'))


if __name__ == '__main__':
    unittest.main()
