from mongoengine import Document, StringField, FloatField

class ProductEntities(Document):
    """A class used to represent a Product that will be delivered"""

    name: str = StringField(required=True)
    weight: float = FloatField(required=True)
