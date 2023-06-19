from abc import ABC, abstractmethod
from typing import Type
from ...views.http_types.http_request import HttpRequest
from ...views.http_types.http_response import HttpResponse


class ViewInterface(ABC):

    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        pass
