from order import Order, OrderLine, Product

def test_order():
    # Setup (actual object)
    order = Order(7)
    order.lines.append(OrderLine(Product('dvd', 1799), 3))
    order.lines.append(OrderLine(Product('cd', 1299), 2))

    # Verify
    expected = create_order()
    assert_equals_order(expected, order)


# TODO: Implement custom assertion methods



# Creation method (create expected object)

def create_order():
    order = Order(7)
    order.lines.append(OrderLine(Product('dvd', 1799), 3))
    order.lines.append(OrderLine(Product('cd', 1299), 2))
    return order
