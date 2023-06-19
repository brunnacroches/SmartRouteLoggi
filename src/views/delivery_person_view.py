from ..controllers.interfaces.delivery_person_controller_interface import DeliveryPersonControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class DeliveryPersonView(ViewInterface):
    def __init__(self, use_case: DeliveryPersonControllerInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        data = http_request.body

        response = self.__use_case.create_delivery_person(data)

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