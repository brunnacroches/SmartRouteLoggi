import unittest
from unittest.mock import Mock, patch
from .product_controller import ProductController

class TestProductController(unittest.TestCase):
    def setUp(self):
        self.product_repository = Mock()
        self.product_controller = ProductController(self.product_repository)
        
    def test_create_product(self):
        data = {'name': 'product_name', 'weight': 10.0}
        self.product_repository.create_product.return_value = data
        response = self.product_controller.create_product(data)
        self.product_repository.create_product.assert_called_once_with(data['name'], data['weight'])
        self.assertEqual(response, {'data': data})

    def test_get_product(self):
        data = {'name': 'product_name', 'weight': 10.0}
        self.product_repository.get_product_by_id.return_value = data
        response = self.product_controller.get_product('123')
        self.product_repository.get_product_by_id.assert_called_once_with('123')
        self.assertEqual(response, {'data': data})

    def test_update_product(self):
        data = {'name': 'updated_name', 'weight': 20.0}
        self.product_repository.update_product.return_value = data
        response = self.product_controller.update_product('123', data)
        self.product_repository.update_product.assert_called_once_with('123', **data)
        self.assertEqual(response, {'data': data})

    def test_delete_product(self):
        self.product_repository.delete_product.return_value = True
        response = self.product_controller.delete_product('123')
        self.product_repository.delete_product.assert_called_once_with('123')
        self.assertEqual(response, {'message': 'Produto com id 123 foi excluído com sucesso.'})


if __name__ == '__main__':
    unittest.main()
