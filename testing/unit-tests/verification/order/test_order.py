from order import Order, OrderLine, Product

def test_order():
    # Setup (actual object)
    order = Order(7)
    order.lines.append(OrderLine(Product('dvd', 1799), 3))
    order.lines.append(OrderLine(Product('cd', 1299), 2))

    # Verify
    expected = create_order()
    assert_equals_order(expected, order)


# Custum assertion methods

def assert_equal_product(expected: Product, actual: Product) -> None:
    assert expected.description == actual.description, 'different Product.description'
    assert expected.price == actual.price, 'different Product.price'

def assert_equal_order_line(expected: OrderLine, actual: OrderLine, msg='') -> None:
    assert expected.quantity == actual.quantity, 'different OrderLine.quantity' + msg
    assert_equal_product(expected.product, actual.product)

def assert_equals_order(expected: Order, actual: Order) -> None:
    assert expected.oid == actual.oid
    assert len(expected.lines) == len(actual.lines)
    length = len(expected.lines)
    for i in range(length):
        assert_equal_order_line(expected.lines[i], actual.lines[i], ' in line: ' + str(i))


# Creation method (create expected object)

def create_order():
    order = Order(7)
    order.lines.append(OrderLine(Product('dvd', 1799), 3))
    order.lines.append(OrderLine(Product('cd', 1299), 2))
    return order
