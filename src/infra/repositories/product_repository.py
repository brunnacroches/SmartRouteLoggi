from ..entities.product_entities import ProductEntities
from ..interfaces.product_repository_interface import ProductRepositoryInterface
from ..interfaces.db_connection_interface import DBConnectionInterface
from bson.objectid import ObjectId
from typing import Dict, List

class ProductRepository(ProductRepositoryInterface):
    """Repository interface for Products, providing basic CRUD operations."""
    def __init__(self, db_connection: DBConnectionInterface) -> None:
        self.__collection_name = 'products'
        self.__db_connection = db_connection

    def create_product(self, name: str, weight: float) -> ProductEntities:
        """Creates a new product with the given name and weight."""
        collection = self.__db_connection.get_collection(self.__collection_name)
        product = {'name': name, 'weight': weight}
        collection.insert_one(product)
        return product

    def get_product_by_id(self, id: str) -> ProductEntities:
        """Retrieves a product by its ID."""
        collection = self.__db_connection.get_collection(self.__collection_name)
        product = collection.find_one({'_id': ObjectId(id)})
        return product

    def update_product(self, id: str, **kwargs) -> ProductEntities:
        """Updates a product identified by its ID with the given fields."""
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one({"_id": ObjectId(id)}, {'$set': kwargs})
        return self.get_product_by_id(id)

    def delete_product(self, id: str) -> None:
        """Deletes a product by its ID. Returns True if deletion was successful, False otherwise."""
        collection = self.__db_connection.get_collection(self.__collection_name)
        result = collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
 