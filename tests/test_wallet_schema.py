import unittest
import unittest.mock as mock
from uuid import UUID
from datetime import datetime


class TestCase(unittest.TestCase):

    @mock.patch('app.utils.iso_datetime')
    @mock.patch('uuid.uuid4')
    def test_load_default(self, m_uuid4, m_iso_datetime):
        m_uuid4.return_value = UUID('87654321876543218765432187654321')
        m_iso_datetime.return_value = '2000-01-02T03:04:05+00:00'

        from app.serializers.wallet_schema import WalletSchema

        schema = WalletSchema(strict=True)
        data, errors = schema.load({
            'client_id': UUID('12345678123456781234567812345678'),
            'currency': 'EUR',
        })

        self.assertDictEqual(errors, {})
        self.assertDictEqual(data, {
            'id': UUID('87654321876543218765432187654321'),
            'is_enabled': True,
            'created_at': datetime(2000, 1, 2, 3, 4, 5),
            'updated_at': datetime(2000, 1, 2, 3, 4, 5),
            'client_id': UUID('12345678123456781234567812345678'),
            'currency': 'EUR',
        })


if __name__ == '__main__':
    unittest.main()
