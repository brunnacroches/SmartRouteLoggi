from cerberus import Validator
from ..errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def validate_delivery_person_data(data):
    schema = {
        "name": {"type": "string", "required": True, "empty": False},
        "routes": {"type": "list", "required": True, "empty": True},
    }

    validator = Validator(schema)
    is_valid = validator.validate(data)

    if not is_valid:
        raise HttpUnprocessableEntityError(validator.errors)