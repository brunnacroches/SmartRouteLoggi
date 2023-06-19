import pytest
from unittest.mock import Mock, MagicMock
from bson.objectid import ObjectId

from ...infra.configs.connection import DBConnectionHandler
from ...infra.repositories.routes_repository import RouteRepository
from ...infra.entities.routes_entities import RouteEntities
from ...infra.entities.product_entities import ProductEntities

@pytest.fixture
def route_repository():
    # Tool's connection with test database
    db_connection = DBConnectionHandler()
    db_connection.connect_to_db()
    connection = db_connection.get_db_connection()

    # Return the RouteRepository with connection on test database
    return RouteRepository(connection)

def test_create_route(route_repository):
    # Create some product entities
    products = [
        ProductEntities(name="Product1", weight=1.2),
        ProductEntities(name="Product2", weight=1.5),
        ProductEntities(name="Product3", weight=1.3),
    ]

    # Now call the method with the list of ProductEntities
    route = route_repository.create_route(api_provider='Provider Test', predicted_duration=1.5, products=products)
    
    assert route.api_provider == 'Provider Test'
    assert route.predicted_duration == 1.5
    assert len(route.products) == len(products)

def test_get_route_by_id(route_repository):
    # Mock the database connection in the existing instance of route_repository
    mock_db_connection = Mock()

    # Mock the collection
    mock_collection = Mock()
    mock_db_connection.get_collection.return_value = mock_collection

    # Modify the database connection in the existing instance of route_repository
    route_repository._RouteRepository__db_connection = mock_db_connection

    # Mock the return of the call to find_one
    mock_route = {
        '_id': '507f1f77bcf86cd799439011',
        'api_provider': 'Provider Test',
        'predicted_duration': 1.5,
        'products': [
            {'name': 'Product1', 'weight': 1.2},
            {'name': 'Product2', 'weight': 1.5},
            {'name': 'Product3', 'weight': 1.3}
        ]
    }
    mock_collection.find_one.return_value = mock_route

    # Test the method get_route_by_id
    route = route_repository.get_route_by_id(id='507f1f77bcf86cd799439011')

    # Perform the asserts
    assert route['_id'] == '507f1f77bcf86cd799439011'
    assert route['api_provider'] == 'Provider Test'
    assert route['predicted_duration'] == 1.5
    assert len(route['products']) == 3


def test_update_route(route_repository):
    # Mock the database connection in the existing instance of route_repository
    mock_db_connection = Mock()

    # Mock the collection
    mock_collection = Mock()
    mock_db_connection.get_collection.return_value = mock_collection

    # Modify the database connection in the existing instance of route_repository
    route_repository._RouteRepository__db_connection = mock_db_connection

    # Define the return of the call to get_route_by_id
    mock_updated_route = {
        '_id': '507f1f77bcf86cd799439011',
        'api_provider': 'Updated Provider',
        'predicted_duration': 2.0,
        'products': [
            {'name': 'Product1', 'weight': 1.2},
            {'name': 'Product2', 'weight': 1.5},
        ]
    }
    route_repository.get_route_by_id = MagicMock(return_value=mock_updated_route)

    # Test the method update_route
    updated_route = route_repository.update_route(
        id='507f1f77bcf86cd799439011',
        api_provider='Updated Provider',
        predicted_duration=2.0
    )

    # Perform the asserts
    assert updated_route['_id'] == '507f1f77bcf86cd799439011'
    assert updated_route['api_provider'] == 'Updated Provider'
    assert updated_route['predicted_duration'] == 2.0
    assert len(updated_route['products']) == 2

def test_delete_route(route_repository):
    # Mock the database connection in the existing instance of route_repository
    mock_db_connection = Mock()

    # Mock the collection
    mock_collection = Mock()
    mock_db_connection.get_collection.return_value = mock_collection

    # Modify the database connection in the existing instance of route_repository
    route_repository._RouteRepository__db_connection = mock_db_connection

    # Test the method delete_route
    route_repository.delete_route(id='507f1f77bcf86cd799439011')

    # Assert that delete_one was called on the collection with the correct argument
    mock_collection.delete_one.assert_called_once_with({"_id": ObjectId('507f1f77bcf86cd799439011')})