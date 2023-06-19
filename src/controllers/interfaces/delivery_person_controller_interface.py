from abc import ABC, abstractmethod
from typing import Dict


class DeliveryPersonControllerInterface(ABC):

    @abstractmethod
    def create_delivery_person(self):
        pass

    @abstractmethod
    def get_delivery_person(self, id):
        pass

    @abstractmethod
    def update_delivery_person(self, id):
        pass

    @abstractmethod
    def delete_delivery_person(self, id):
        pass
