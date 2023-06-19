from ...infra.repositories.product_repository import ProductRepository
from ...controllers.product_controller import ProductController
from ...views.product_view import ProductView

def delivery_person_compose():
    model = ProductRepository()
    controller = ProductController(model)
    view = ProductView(controller)

    return view