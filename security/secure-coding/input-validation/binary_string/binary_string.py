import re


class ValidationError(Exception):
    pass


def operation(data):
    print(data)
    pattern = '^[01]{2,4}$'  # Regular expression
    result = re.match(pattern, data)
    if result:
        return int(data, 2)
    else:
        raise ValidationError('Invalid data value!')
