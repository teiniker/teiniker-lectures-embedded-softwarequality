import re


class ValidationError(Exception):
    pass

# Regular expression pattern to match a valid hexadecimal string 
# (2 to 4 characters, uppercase letters and digits)
PATTERN = '^[A-F0-9]{2,4}$'

def operation(data):
    result = re.match(PATTERN, data)
    if not result:
        raise ValidationError('Invalid data value!')

    # Business logic
