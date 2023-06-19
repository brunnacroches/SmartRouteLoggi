import unittest
from unittest.mock import Mock
from ..validators.products_validators import validate_product_data, HttpUnprocessableEntityError


class TestProductValidator(unittest.TestCase):
    def test_valid_product_data(self):
        data = {
            "name": "Product 1",
            "weight": 1.5
        }
        self.assertIsNone(validate_product_data(data))

    def test_invalid_product_data(self):
        data = {
            "name": "",
            "weight": -2.0
        }
        with self.assertRaises(HttpUnprocessableEntityError):
            validate_product_data(data)
