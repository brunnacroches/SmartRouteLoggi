from ..controllers.tests.product_controller_spy import ProductControllerSpy
from ..views.http_types.http_request import HttpRequest
from ..views.http_types.http_response import HttpResponse
from ..views.product_view import ProductView

class HttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "name": "New Product",
            "weight": 1.5
        }


def test_handler():
    http_request_mock = HttpRequestMock()
    controller = ProductControllerSpy()
    view = ProductView(controller)

    response = view.handle(HttpRequest(http_request_mock.body))

    assert controller.create_product_attributes == http_request_mock.body

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"]["attributes"] is not None