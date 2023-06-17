from typing import List
from mongoengine import Document, StringField, ListField, ReferenceField
from .routes_entities import RouteEntities

class DeliveryPersonEntities(Document):
    """A class used to represent a Delivery Person who will deliver Products on certain Routes"""

    name: str = StringField(required=True)
    routes: List[ReferenceField(RouteEntities)] = ListField(ReferenceField(RouteEntities))