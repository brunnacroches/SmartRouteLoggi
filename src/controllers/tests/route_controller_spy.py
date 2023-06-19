from typing import Dict

class RouteControllerSpy:
    def __init__(self) -> None:
        self.create_route_attributes = {}

    def create_route(self, data: Dict) -> Dict:
        self.create_route_attributes = data
        return {
            "data": {
                "name": "newRouteName",
                "api_provider": "Provider",
                "predicted_duration": 10.0,
                "products": [],
            }
        }