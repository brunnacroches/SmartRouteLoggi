from abc import ABC, abstractmethod
from ...infra.entities.delivery_person_entities import DeliveryPersonEntities
from ...infra.entities.routes_entities import RouteEntities
from typing import List


class DeliveryPersonInterface(ABC):
    @abstractmethod
    def create_delivery_person(self, name: str, routes: List[RouteEntities]) -> DeliveryPersonEntities:
        """Method to create a Delivery"""
        pass 

    @abstractmethod
    def get_delivery_person_by_id(self, id: str) -> DeliveryPersonEntities:
        """Method to get a Delivery by id"""
        pass

    @abstractmethod
    def update_delivery_person(self, id: str, **kwargs) -> DeliveryPersonEntities:
        """Method to update a Delivery"""
        pass

    @abstractmethod
    def delete_delivery_person(self, id: str) -> None:
        """Method to delete a Delivery"""
        pass
