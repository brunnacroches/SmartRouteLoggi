from ..controllers.interfaces.routes_controller_interface import RoutesControllerInterface
from ..views.http_types.http_request import HttpRequest
from ..views.http_types.http_response import HttpResponse
from ..views.interfaces.view_interface import ViewInterface


class RoutesView(ViewInterface):
    def __init__(self, use_case: RoutesControllerInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        data = http_request.body

        response = self.__use_case.create_route(data)

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "Products",
                    "count": 1,
                    "attributes": response['data'],
                }
            }
        )