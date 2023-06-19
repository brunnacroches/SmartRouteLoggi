from abc import ABC, abstractmethod
from typing import Dict


class ProductControllerInterface(ABC):
    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def get_product(self, id):
        pass

    @abstractmethod
    def update_product(self, id):
        pass

    @abstractmethod
    def delete_product(self, id):
        pass
