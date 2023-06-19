from cerberus import Validator
from ..errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def validate_product_data(data):
    schema = {
        "name": {"type": "string", "required": True, "empty": False},
        "weight": {"type": "float", "required": True, "empty": False, "min": 0},
    }

    validator = Validator(schema)
    is_valid = validator.validate(data)

    if not is_valid:
        raise HttpUnprocessableEntityError(validator.errors)
