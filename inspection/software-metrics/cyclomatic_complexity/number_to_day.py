def convert_number_to_day(num):
    result = ""
    if num == 1:
        result = "Monday"
    elif num == 2:
        result = "Tuesday"
    elif num == 3:
        result = "Wednesday"
    elif num == 4:
        result = "Thursday"
    elif num == 5:
        result = "Friday"
    elif num == 6:
        result = "Saturday"
    elif num == 7:
        result = "Sunday"
    else:
        result = "Invalid day!"
    return result

assert convert_number_to_day(1) == "Monday"
assert convert_number_to_day(2) == "Tuesday"
assert convert_number_to_day(3) == "Wednesday"
assert convert_number_to_day(4) == "Thursday"
assert convert_number_to_day(5) == "Friday"
assert convert_number_to_day(6) == "Saturday"
assert convert_number_to_day(7) == "Sunday"
assert convert_number_to_day(8) == "Invalid day!"
