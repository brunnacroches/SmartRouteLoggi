from typing import List
from mongoengine import Document, StringField, ListField, ReferenceField, FloatField
from .product_entities import Product

class RouteEntities(Document):
    """A class used to represent a Delivery Route"""

    api_provider: str = StringField(required=True)
    predicted_duration: float = FloatField(required=True)
    actual_duration: float = FloatField()
    products: List[ReferenceField(Product)] = ListField(ReferenceField(Product))
