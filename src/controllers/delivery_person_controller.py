from typing import Dict, List
from ..infra.interfaces.delivery_repository_interface import DeliveryPersonInterface
from .interfaces.delivery_person_controller_interface import DeliveryPersonControllerInterface
from ..infra.entities.routes_entities import RouteEntities

class DeliveryPersonController(DeliveryPersonControllerInterface):
    def __init__(self, delivery_person: DeliveryPersonInterface):
        self.__delivery_person_repository = delivery_person
    
    def create_delivery_person(self, name: str, routes: List[RouteEntities]) -> Dict:
        new_delivery_person = self.__delivery_person_repository.create_delivery_person(name, routes)
        if not new_delivery_person:
            raise Exception('Ocorreu um erro na criação da pessoa de entrega, tente novamente')
        return self.__format_response(new_delivery_person)

    def get_delivery_person(self, id: str) -> Dict:
        delivery_person = self.__delivery_person_repository.get_delivery_person_by_id(id)
        if not delivery_person:
            raise Exception(f'Pessoa de entrega com id {id} não encontrada.')
        return self.__format_response(delivery_person)

    def update_delivery_person(self, id: str, data: Dict) -> Dict:
        updated_delivery_person = self.__delivery_person_repository.update_delivery_person(id, **data)
        if not updated_delivery_person:
            raise Exception(f'Ocorreu um erro ao atualizar a pessoa de entrega com id {id}.')
        return self.__format_response(updated_delivery_person)

    def delete_delivery_person(self, id: str) -> Dict:
        result = self.__delivery_person_repository.delete_delivery_person(id)
        if not result:
            raise Exception(f'Ocorreu um erro ao excluir a pessoa de entrega com id {id}.')
        return {"message": f'Pessoa de entrega com id {id} foi excluída com sucesso.'}

    def __format_response(self, delivery_person: object) -> Dict:
        return {
            "data": {
                "name": delivery_person['name'],
                "routes": delivery_person['routes'],
            }
        }