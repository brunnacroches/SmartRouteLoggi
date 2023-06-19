from ...infra.repositories.routes_repository import RouteRepository
from ...controllers.routes_controller import RouteController
from ...views.routes_view import RoutesView

def delivery_person_compose():
    model = RouteRepository()
    controller = RouteController(model)
    view = RoutesView(controller)

    return view