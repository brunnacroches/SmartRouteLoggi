from typing import Dict

class ProductControllerSpy:
    def __init__(self) -> None:
        self.create_product_attributes = {}

    def create_product(self, data: Dict) -> Dict:
        self.create_product_attributes = data
        return {
            "data": {
                "name": "newProductName",
                "weight": 1.5,
            }
        }