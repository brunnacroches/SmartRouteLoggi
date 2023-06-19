from ...infra.entities.delivery_person_entities import DeliveryPersonEntities
from ..entities.delivery_person_entities import DeliveryPersonEntities
from ..interfaces.delivery_repository_interface import DeliveryPersonInterface
from ..interfaces.db_connection_interface import DBConnectionInterface
from bson.objectid import ObjectId
from typing import List
from ...infra.entities.routes_entities import RouteEntities


class DeliveryPersonRepository(DeliveryPersonInterface):
    def __init__(self, db_connection: DBConnectionInterface) -> None:
        self.__collection_name = 'deliveryPerson'
        self.__db_connection = db_connection

    def create_delivery_person(self, name: str, routes: List[RouteEntities]) -> DeliveryPersonEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        delivery = {'name': name, 'routes': [str(route.id) for route in routes]}
        collection.insert_one(delivery)
        return DeliveryPersonEntities(name=name, routes=routes)

    def get_delivery_person_by_id(self, id: str) -> DeliveryPersonEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        delivery = collection.find_one({'_id': ObjectId(id)})
        return delivery

    def update_delivery_person(self, id: str, **kwargs) -> DeliveryPersonEntities:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({'_id': ObjectId(id)}, {'$set': kwargs})
        return self.get_delivery_person_by_id(id)

    def delete_delivery_person(self, id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId(id)})