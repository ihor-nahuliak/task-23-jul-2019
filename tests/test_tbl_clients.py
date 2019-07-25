import unittest

import sqlalchemy as sa
from quicksets import settings

from app.tables.meta import metadata
from app.tables.tbl_clients import tbl_clients


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metadata.bind = sa.engine.create_engine(settings.POSTGRESQL_URL)

    def test_tbl_clients_exists(self):
        self.assertTrue(tbl_clients.exists())


if __name__ == '__main__':
    unittest.main()
