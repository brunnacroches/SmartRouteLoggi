from mongoengine import Document, StringField, FloatField

class Product(Document):
    """A class used to represent a Product that will be delivered"""

    name = StringField(required=True)
    weight = FloatField(required=True)
