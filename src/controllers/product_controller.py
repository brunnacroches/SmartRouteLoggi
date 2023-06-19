from typing import Dict
from ..infra.interfaces.product_repository_interface import ProductRepositoryInterface
from .interfaces.product_controller_interface import ProductControllerInterface

class ProductController(ProductControllerInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.__product_repository = product_repository

    def create_product(self, data: Dict) -> Dict:
        new_product = self.__product_repository.create_product(data['name'], data['weight'])
        if not new_product: 
            raise Exception('Ocorreu um erro na criação do produto, tente novamente')
        return self.__format_response(new_product)

    def get_product(self, id: str) -> Dict:
        product = self.__product_repository.get_product_by_id(id)
        if not product:
            raise Exception(f'Produto com id {id} não encontrado.')
        return self.__format_response(product)

    def update_product(self, id: str, data: Dict) -> Dict:
        updated_product = self.__product_repository.update_product(id, **data)
        if not updated_product:
            raise Exception(f'Ocorreu um erro ao atualizar o produto com id {id}.')
        return self.__format_response(updated_product)

    def delete_product(self, id: str) -> Dict:
        result = self.__product_repository.delete_product(id)
        if not result:
            raise Exception(f'Ocorreu um erro ao excluir o produto com id {id}.')
        return {"message": f'Produto com id {id} foi excluído com sucesso.'}

    def __format_response(self, product: Dict) -> Dict:
        return {
            "data": {
                "name": product['name'],
                "weight": product['weight'],
            }
        }