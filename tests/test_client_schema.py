import unittest
import unittest.mock as mock
from uuid import UUID
from datetime import datetime


class TestCase(unittest.TestCase):

    @mock.patch('app.utils.iso_datetime')
    @mock.patch('uuid.uuid4')
    def test_load_default(self, m_uuid4, m_iso_datetime):
        m_uuid4.return_value = UUID('12345678123456781234567812345678')
        m_iso_datetime.return_value = '2000-01-02T03:04:05+00:00'

        from app.serializers.client_schema import ClientSchema

        schema = ClientSchema(strict=True)
        data, errors = schema.load({})

        self.assertDictEqual(errors, {})
        self.assertDictEqual(data, {
            'id': UUID('12345678123456781234567812345678'),
            'is_enabled': True,
            'created_at': datetime(2000, 1, 2, 3, 4, 5),
            'updated_at': datetime(2000, 1, 2, 3, 4, 5),
            'name': None,
            'country': None,
            'city': None
        })


if __name__ == '__main__':
    unittest.main()
