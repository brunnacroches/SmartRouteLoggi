import unittest
from unittest.mock import Mock
from ..validators.delivery_person_validators import validate_delivery_person_data, HttpUnprocessableEntityError


class TestDeliveryPersonValidator(unittest.TestCase):
    def test_valid_delivery_person_data(self):
        data = {
            "name": "John Doe",
            "routes": []
        }
        self.assertIsNone(validate_delivery_person_data(data))

    def test_invalid_delivery_person_data(self):
        data = {
            "name": "",
            "routes": None
        }
        with self.assertRaises(HttpUnprocessableEntityError):
            validate_delivery_person_data(data)


if __name__ == '__main__':
    unittest.main()
