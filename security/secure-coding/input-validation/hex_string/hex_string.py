import re


class ValidationError(Exception):
    pass


def operation(data):
    # print(data)
    pattern = '^[A-F0-9]{2,4}$'  # Regular expression
    result = re.match(pattern, data)
    if result:
        return int(data, 16)
    else:
        raise ValidationError('Invalid data value!')
