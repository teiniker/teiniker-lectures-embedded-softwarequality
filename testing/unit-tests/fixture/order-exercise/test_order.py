
class TestOrder:

    def test_delegation_fixture(self):
        # Setup
        order = self.create_order()
        # Exercise

        # Verify
        assert 7 == order.oid

        assert 3 == order.lines[0].quantity
        assert 'dvd' == order.lines[0].product.description
        assert 1799 == order.lines[0].product.price

        assert 2 == order.lines[1].quantity
        assert 'cd' == order.lines[1].product.description
        assert 1299 == order.lines[1].product.price

    # TODO: Implement custom creation method
