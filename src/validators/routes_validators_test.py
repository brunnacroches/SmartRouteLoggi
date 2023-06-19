import unittest
from unittest.mock import Mock
from ..validators.routes_validators import validate_route_data, HttpUnprocessableEntityError


class TestRouteValidator(unittest.TestCase):
    def test_valid_route_data(self):
        data = {
            "api_provider": "Provider",
            "predicted_duration": 10.0,
            "actual_duration": 8.5,
            "products": ["product1", "product2"]
        }
        self.assertIsNone(validate_route_data(data))

    def test_invalid_route_data(self):
        data = {
            "api_provider": "",
            "predicted_duration": -5.0,
            "actual_duration": -3.0,
            "products": []
        }
        with self.assertRaises(HttpUnprocessableEntityError):
            validate_route_data(data)

