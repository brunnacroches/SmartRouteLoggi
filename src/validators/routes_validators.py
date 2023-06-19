from cerberus import Validator
from ..errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def validate_route_data(data):
    schema = {
        "api_provider": {"type": "string", "required": True, "empty": False},
        "predicted_duration": {"type": "float", "required": True, "empty": False, "min": 0},
        "actual_duration": {"type": "float", "required": False, "min": 0},
        "products": {"type": "list", "required": True, "empty": False},
    }

    validator = Validator(schema)
    is_valid = validator.validate(data)

    if not is_valid:
        raise HttpUnprocessableEntityError(validator.errors)
