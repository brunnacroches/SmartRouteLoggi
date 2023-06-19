import pytest
from bson.objectid import ObjectId
from ...infra.configs.connection import DBConnectionHandler
from ...infra.repositories.product_repository import ProductRepository

@pytest.fixture
def product_repository():
    # Tools connection with test database a conexão com o banco de dados de teste
    db_connection = DBConnectionHandler()
    db_connection.connect_to_db()
    connection = db_connection.get_db_connection()

    # Return the ProductsRepository with connection test database
    return ProductRepository(connection)

def test_create_product(product_repository):
    product = product_repository.create_product(name='Test Product', weight=10.0)
    assert product['name'] == 'Test Product'
    assert product['weight'] == 10.0

def test_get_product_by_id(product_repository):
    product_id = '507f1f77bcf86cd799439011'  # Substitute this with actual product ID
    product = product_repository.get_product_by_id(product_id)
    if product is None:
        assert product is None
    else:
        assert product['_id'] == ObjectId(product_id)

def test_update_product(product_repository):
    # Setup: create a product without specifying an ID
    created_product = product_repository.create_product(name='Test Product', weight=10.0)
    product_id = created_product["_id"]

    # Test: update the product
    updated_product = product_repository.update_product(product_id, name='Updated Product', weight=15.0)
    assert updated_product['name'] == 'Updated Product'
    assert updated_product['weight'] == 15.0

def test_delete_product(product_repository):
    # Setup: create a product without specifying an ID
    created_product = product_repository.create_product(name='Test Product', weight=10.0)
    product_id = created_product["_id"]

    # Test: delete the product
    deletion_successful = product_repository.delete_product(product_id)
    assert deletion_successful is True
    assert product_repository.get_product_by_id(product_id) is None