import pytest
from unittest.mock import Mock, MagicMock
from bson.objectid import ObjectId
from ...infra.configs.connection import DBConnectionHandler
from ...infra.repositories.delivery_repository import DeliveryPersonRepository
from ...infra.entities.routes_entities import RouteEntities
from ...infra.entities.product_entities import ProductEntities
from ...infra.entities.delivery_person_entities import DeliveryPersonEntities

@pytest.fixture
def delivery_repository():
    # Tools connectin with test database
    db_connection = DBConnectionHandler()
    db_connection.connect_to_db()
    connection = db_connection.get_db_connection()

    # Return the deliverysRepository with connection on test database
    return DeliveryPersonRepository(connection)

def test_create_delivery(delivery_repository):
    # Create some product entities
    products = [
        ProductEntities(name="Product1", weight=1.2),
        ProductEntities(name="Product2", weight=1.5),
        ProductEntities(name="Product3", weight=1.3),
    ]
    
    # Create some route entities
    routes = [
        RouteEntities(api_provider="Provider1", predicted_duration=1.2, products=products), 
        RouteEntities(api_provider="Provider2", predicted_duration=1.5, products=products), 
        RouteEntities(api_provider="Provider3", predicted_duration=1.3, products=products)
    ] 

    # Now call the method with the list of RouteEntities
    delivery = delivery_repository.create_delivery_person(name='Test delivery', routes=routes)
    
    assert delivery['name'] == 'Test delivery'
    assert len(delivery['routes']) == len(routes)

def test_get_delivery_by_id(delivery_repository):
    # Create some mock data to insert into the collection
    delivery_id = ObjectId()
    name = 'Entrega de teste'
    routes = [
        {
            'api_provider': 'Provider1',
            'predicted_duration': 1.2,
            'products': [
                {'name': 'Product1', 'weight': 1.2},
                {'name': 'Product2', 'weight': 1.5},
                {'name': 'Product3', 'weight': 1.3}
            ]
        },
        {
            'api_provider': 'Provider2',
            'predicted_duraction': 1.5,
            'products': [
                {'name': 'Product4', 'weight': 1.4},
                {'name': 'Product5', 'weight': 1.7}
            ]
        }
    ]
    # Insert the mock data into the collection
    collection = delivery_repository._DeliveryPersonRepository__db_connection.get_collection(delivery_repository._DeliveryPersonRepository__collection_name)
    delivery_data = {'_id': delivery_id, 'name': name, 'routes': routes}
    collection.insert_one(delivery_data)
    
    # Call the method with the delivery ID
    delivery = delivery_repository.get_delivery_person_by_id(id=str(delivery_id))
    
    if delivery is not None:
        assert str(delivery['_id']) == str(delivery_id)
        assert delivery['name'] == name
        assert len(delivery['routes']) == len(routes)
    else:
        assert False, 'Delivery not found for the given ID'

def test_update_delivery_person(delivery_repository):
    # Cria um mock para a conexão com o banco de dados
    mock_db_connection = Mock()

    # Cria um mock para a coleção
    mock_collection = Mock()
    mock_db_connection.get_collection.return_value = mock_collection

    # Modifica a conexão do banco de dados na instância existente de delivery_repository
    delivery_repository._DeliveryPersonRepository__db_connection = mock_db_connection

    # Define o retorno da chamada a get_delivery_person_by_id
    mock_updated_delivery = {
        '_id': '507f1f77bcf86cd799439011',
        'name': 'Entrega Atualizada',
        'routes': [
            {
                'api_provider': 'Provider1',
                'predicted_duration': 1.2,
                'products': []
            },
            {
                'api_provider': 'Provider2',
                'predicted_duration': 1.5,
                'products': []
            }
        ]
    }
    delivery_repository.get_delivery_person_by_id = MagicMock(return_value=mock_updated_delivery)

    # Testa o método update_delivery_person
    updated_delivery = delivery_repository.update_delivery_person(
        id='507f1f77bcf86cd799439011',
        name='Entrega Atualizada',
        routes=[...]
    )

    # Realiza os asserts
    assert updated_delivery['name'] == 'Entrega Atualizada'
    assert len(updated_delivery['routes']) == 2

def test_delete_delivery_person(delivery_repository):
    # Mock the database connection in the existing instance of delivery_repository
    mock_db_connection = Mock()

    # Mock the collection
    mock_collection = Mock()
    mock_db_connection.get_collection.return_value = mock_collection

    # Modify the database connection in the existing instance of delivery_repository
    delivery_repository._DeliveryPersonRepository__db_connection = mock_db_connection

    # Mock the return of the call to get_delivery_person_by_id
    mock_delivery = {
        '_id': '507f1f77bcf86cd799439011',
        'name': 'Entrega Atualizada',
        'routes': [
            {
                'api_provider': 'Provider1',
                'predicted_duration': 1.2,
                'products': []
            },
            {
                'api_provider': 'Provider2',
                'predicted_duration': 1.5,
                'products': []
            }
        ]
    }

    # Define a function that will simulate the change in the return value after deletion
    def get_delivery_side_effect(id):
        if mock_collection.delete_one.called:
            return None
        else:
            return mock_delivery

    delivery_repository.get_delivery_person_by_id = MagicMock(side_effect=get_delivery_side_effect)

    # Test the method delete_delivery_person
    delivery_repository.delete_delivery_person(id='507f1f77bcf86cd799439011')

    # Perform the asserts
    # Assert that delete_one was called on the collection with the correct argument
    mock_collection.delete_one.assert_called_once_with({"_id": ObjectId('507f1f77bcf86cd799439011')})

    # Assert that get_delivery_person_by_id now returns None for the deleted id
    assert delivery_repository.get_delivery_person_by_id(id='507f1f77bcf86cd799439011') is None
