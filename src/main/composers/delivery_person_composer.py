from ...infra.repositories.delivery_repository import DeliveryPersonRepository
from ...controllers.delivery_person_controller import DeliveryPersonController
from ...views.delivery_person_view import DeliveryPersonView

def delivery_person_compose():
    model = DeliveryPersonRepository()
    controller = DeliveryPersonController(model)
    view = DeliveryPersonView(controller)

    return view