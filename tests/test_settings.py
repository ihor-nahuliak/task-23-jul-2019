import unittest

from quicksets import settings


class TestCase(unittest.TestCase):

    def test_root_path_is_absolute(self):
        self.assertTrue(settings.ROOT_PATH.startswith('/'))

    def test_root_path_is_app_dir(self):
        self.assertTrue(settings.ROOT_PATH.endswith('/app'))

    def test_templates_path_is_in_app_dir(self):
        self.assertTrue(settings.TEMPLATES_PATH.endswith('/app/templates'))

    def test_postgresql_url(self):
        self.assertEqual(
            settings.POSTGRESQL_URL,
            'postgresql+psycopg2://postgres:@localhost:5432'
            '/task23jul2019_testing'
        )


if __name__ == '__main__':
    unittest.main()
