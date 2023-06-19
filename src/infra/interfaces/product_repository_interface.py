from abc import ABC, abstractmethod
from ...infra.entities.product_entities import ProductEntities

class ProductRepositoryInterface(ABC):
    """
    ProductRepositoryInterface is a generic abstract base class that specifies the
    basic CRUD operations that a repository should implement.
    """

    @abstractmethod
    def create_product(self, name: str, weight: float) -> ProductEntities:
        """
        Create a new document in the database.
        """
        pass

    @abstractmethod
    def get_product_by_id(self, id: str) -> ProductEntities:
        """
        Retrieve a document from the database by its ID.
        """
        pass

    @abstractmethod
    def update_product(self, name: str, **kwargs) -> ProductEntities:
        """
        Update a document in the database.
        """
        pass

    @abstractmethod
    def delete_product(self, id: str) -> None:
        """
        Delete a document from the database.
        """
        pass
