from typing import List
from bson.objectid import ObjectId

from ...infra.entities.product_entities import ProductEntities
from ...infra.entities.routes_entities import RouteEntities
from ..interfaces.db_connection_interface import DBConnectionInterface
from ..interfaces.routes_repository_interface import RoutesInterface
from ...infra.entities.routes_entities import RouteEntities
from ...infra.entities.product_entities import ProductEntities

class RouteRepository(RoutesInterface):
    def __init__(self, db_connection: DBConnectionInterface) -> None:
        self.__collection_name = 'routes'
        self.__db_connection = db_connection

    def create_route(self, api_provider: str, predicted_duration: float, products: List[ProductEntities]) -> RouteEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        route = {
                'api_provider': api_provider, 
                 'predicted_duration': predicted_duration, 
                 'products': [str(product.id) for product in products]}
        collection.insert_one(route)
        return RouteEntities(api_provider=api_provider, predicted_duration=predicted_duration, products=products)

    def get_route_by_id(self, id: str) -> RouteEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        route_dict = collection.find_one({'_id': ObjectId(id)})
        return route_dict

    def update_route(self, id: str, **kwargs) -> RouteEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update({'_id': ObjectId(id)}, {'$set': kwargs})
        return self.get_route_by_id(id)

    def delete_route(self, id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({'_id': ObjectId(id)})