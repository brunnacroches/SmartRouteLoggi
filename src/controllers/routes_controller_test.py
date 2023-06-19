import unittest
from unittest.mock import Mock
from typing import Dict
from .routes_controller import RouteController


class TestRouteController(unittest.TestCase):
    def setUp(self):
        self.route_repository = Mock()
        self.route_controller = RouteController(self.route_repository)
        
    def test_create_route(self):
        data = {'api_provider': 'Provider', 'predicted_duration': 10.0, 'products': []}
        new_route = Mock()
        new_route.id = '123'
        new_route.api_provider = 'Provider'
        new_route.predicted_duration = 10.0
        new_route.products = []
        self.route_repository.create_route.return_value = new_route
        response = self.route_controller.create_route(data)
        self.route_repository.create_route.assert_called_once_with(data)
        self.assertEqual(response, {'data': {'id': '123', 'api_provider': 'Provider', 'predicted_duration': 10.0, 'products': []}})

    def test_get_route(self):
        data = {'api_provider': 'Provider', 'predicted_duration': 10.0, 'products': []}
        route = Mock()
        route.id = '123'
        route.api_provider = 'Provider'
        route.predicted_duration = 10.0
        route.products = []
        self.route_repository.get_route_by_id.return_value = route
        response = self.route_controller.get_route('123')
        self.route_repository.get_route_by_id.assert_called_once_with('123')
        self.assertEqual(response, {'data': {'id': '123', 'api_provider': 'Provider', 'predicted_duration': 10.0, 'products': []}})

    def test_update_route(self):
        data = {'api_provider': 'Updated Provider', 'predicted_duration': 20.0, 'products': []}
        updated_route = Mock()
        updated_route.id = '123'
        updated_route.api_provider = 'Updated Provider'
        updated_route.predicted_duration = 20.0
        updated_route.products = []
        self.route_repository.update_route.return_value = updated_route
        response = self.route_controller.update_route('123', data)
        self.route_repository.update_route.assert_called_once_with('123', api_provider='Updated Provider', predicted_duration=20.0, products=[])
        self.assertEqual(response, {'data': {'id': '123', 'api_provider': 'Updated Provider', 'predicted_duration': 20.0, 'products': []}})

    def test_delete_route(self):
        self.route_repository.delete_route.return_value = None
        response = self.route_controller.delete_route('123')
        self.route_repository.delete_route.assert_called_once_with('123')
        self.assertEqual(response, {'message': 'Rota com ID 123 foi excluída com sucesso.'})

if __name__ == '__main__':
    unittest.main()