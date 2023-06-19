from abc import ABC, abstractmethod
from typing import List
from ...infra.entities.product_entities import ProductEntities
from ...infra.entities.routes_entities import RouteEntities

class RoutesInterface(ABC):
    @abstractmethod
    def create_route(self, api_provider: str, predicted_duration: float, products: List[ProductEntities]) -> RouteEntities: 
        pass

    @abstractmethod
    def get_route_by_id(self, id: str) -> RouteEntities:
        pass

    @abstractmethod
    def update_route(self, id: str, **kwargs) -> RouteEntities:
        pass

    @abstractmethod
    def delete_route(self, id: str) -> None:
        pass
