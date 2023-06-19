from typing import Dict
from ..infra.interfaces.routes_repository_interface import RoutesInterface
from .interfaces.routes_controller_interface import RoutesControllerInterface
from ..infra.interfaces.routes_repository_interface import RouteEntities

class RouteController(RoutesControllerInterface):
    def __init__(self, route_repository: RoutesInterface):
        self.__route_repository = route_repository

    def create_route(self, data: Dict) -> Dict:
        new_route = self.__route_repository.create_route(data)
        return self.__format_response(new_route)

    def get_route(self, id: str) -> Dict:
        route = self.__route_repository.get_route_by_id(id)
        return self.__format_response(route)

    def update_route(self, id: str, data: Dict) -> Dict:
        updated_route = self.__route_repository.update_route(id, **data)
        return self.__format_response(updated_route)

    def delete_route(self, id: str) -> Dict:
        self.__route_repository.delete_route(id)
        return {"message": f"Rota com ID {id} foi excluída com sucesso."}

    def __format_response(self, route: RouteEntities) -> Dict:
        return {
            "data": {
                "id": str(route.id),
                "api_provider": route.api_provider,
                "predicted_duration": route.predicted_duration,
                "products": [str(product.id) for product in route.products],
            }
        }



