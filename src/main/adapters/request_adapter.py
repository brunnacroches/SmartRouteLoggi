from typing import Callable

from flask import request as FlaskRequest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


def request_adapter(request: FlaskRequest, callback: Callable) -> HttpResponse:
    body = None
    if request.data: body = request.json

    http_request = HttpRequest(
        header=request.headers,
        body=body,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )

    http_response = callback(http_request)
    return http_response
