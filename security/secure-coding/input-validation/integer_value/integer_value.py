
class ValidationError(Exception):
    pass


def operation(value):
    print(f"operation({value})")
    if value < 1 or value > 99:
        raise ValidationError('Invalid data value!')
    return value
