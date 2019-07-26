import unittest

import sqlalchemy as sa
from quicksets import settings

from app.tables.meta import metadata
from app.tables.tbl_payments import tbl_payments


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        metadata.bind = sa.engine.create_engine(settings.POSTGRESQL_URL)

    def test_tbl_payments_exists(self):
        self.assertTrue(tbl_payments.exists())


if __name__ == '__main__':
    unittest.main()
