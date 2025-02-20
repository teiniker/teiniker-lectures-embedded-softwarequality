
data_list :list[str] = []

data_list.append('one')

data_tuple: tuple[str, ...] = ("1", "2")

data_dict: dict[int, str] = {}


def add(value_a:int, value_b:int) -> int:
    return value_a + value_b


assert 2+3 == add(2, 3)
