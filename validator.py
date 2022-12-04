from cerberus import Validator


def validate_inputs(firstName, lastName):
    spec = {'type': 'string', 'required': True,
            'maxlength': 20, 'regex': '[a-zA-Z\s]+$'}
    schema = {'firstName': spec, 'lastName': spec}
    validator = Validator(schema)
    return validator.validate({'firstName': firstName, 'lastName': lastName})
