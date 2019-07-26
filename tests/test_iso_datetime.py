import unittest
import unittest.mock as mock
from datetime import datetime

from app.utils.datetime import iso_datetime


class TestCase(unittest.TestCase):

    @mock.patch('app.utils.datetime.datetime')
    def test_iso_datetime(self, m_datetime):
        m_datetime.utcnow.return_value = datetime(
            year=2000, month=1, day=2, hour=3, minute=4, second=5)

        self.assertEqual(iso_datetime(), '2000-01-02T03:04:05+00:00')


if __name__ == '__main__':
    unittest.main()
