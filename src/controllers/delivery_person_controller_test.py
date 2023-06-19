import unittest
from unittest.mock import Mock
from .delivery_person_controller import DeliveryPersonController

class TestDeliveryPersonController(unittest.TestCase):
    def setUp(self):
        self.delivery_person_repository = Mock()
        self.delivery_person_controller = DeliveryPersonController(self.delivery_person_repository)
        
    def test_create_delivery_person(self):
        data = {'name': 'John Doe', 'routes': ['route1', 'route2']}
        self.delivery_person_repository.create_delivery_person.return_value = data
        response = self.delivery_person_controller.create_delivery_person(data['name'], data['routes'])
        self.delivery_person_repository.create_delivery_person.assert_called_once_with(data['name'], data['routes'])
        self.assertEqual(response, {'data': data})

    def test_get_delivery_person(self):
        data = {'name': 'John Doe', 'routes': ['route1', 'route2']}
        self.delivery_person_repository.get_delivery_person_by_id.return_value = data
        response = self.delivery_person_controller.get_delivery_person('123')
        self.delivery_person_repository.get_delivery_person_by_id.assert_called_once_with('123')
        self.assertEqual(response, {'data': data})

    def test_update_delivery_person(self):
        data = {'name': 'Jane Doe', 'routes': ['route3', 'route4']}
        self.delivery_person_repository.update_delivery_person.return_value = data
        response = self.delivery_person_controller.update_delivery_person('123', data)
        self.delivery_person_repository.update_delivery_person.assert_called_once_with('123', **data)
        self.assertEqual(response, {'data': data})

    def test_delete_delivery_person(self):
        self.delivery_person_repository.delete_delivery_person.return_value = True
        response = self.delivery_person_controller.delete_delivery_person('123')
        self.delivery_person_repository.delete_delivery_person.assert_called_once_with('123')
        self.assertEqual(response, {'message': 'Pessoa de entrega com id 123 foi excluída com sucesso.'})

if __name__ == '__main__':
    unittest.main()
