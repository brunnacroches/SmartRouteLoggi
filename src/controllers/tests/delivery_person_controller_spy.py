from typing import Dict

class DeliveryPersonControllerSpy:
    def __init__(self) -> None:
        self.create_delivery_person_attributes = {}

    def create_delivery_person(self, data: Dict) -> Dict:
        self.create_delivery_person_attributes = data
        return {
            "data": {
                "name": "newDeliveryPersonName",
                "routes": [],
            }
        }