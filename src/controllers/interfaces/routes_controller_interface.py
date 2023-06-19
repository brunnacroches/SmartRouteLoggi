from abc import ABC, abstractmethod
from typing import Dict


class RoutesControllerInterface(ABC):
    @abstractmethod
    def create_route(self):
        pass

    @abstractmethod
    def get_route(self, id):
        pass

    @abstractmethod
    def update_route(self, id):
        pass

    @abstractmethod
    def delete_route(self, id):
        pass
