import unittest
from user_table import UserTable, User 
from user_table_builder import UserTableBuilder

class UserTableTest(unittest.TestCase):
    def setUp(self):
        self.table = UserTable()
        self.table = (UserTableBuilder()
                    .user(3,"Lisa","lKi8/hhgT")
                    .user(7,"Bart","kJ7&fRsd34%7")
                    .build())

    def test_find_by_id(self):
        # Exercise
        actual = self.table.find_by_id(3)
        # Verify
        expected = User(3,"Lisa","lKi8/hhgT")
        self.assertEqualUser(expected, actual)

    def test_find_all(self):
        # Exercise
        users = self.table.find_all()
        # Verify
        self.assertEqual(len(users), 2)
        self.assertEqual(3, users[0].oid)
        self.assertEqual(7, users[1].oid)

    def test_insert_user(self):
        # Exercise
        user = User(11,"Homer","lKfDt54sss6")
        self.table.insert(user)
        # Verify
        self.assertEqual(len(self.table.find_all()), 3)
        users = self.table.find_all()
        self.assertEqual(3, users[0].oid)
        self.assertEqual(7, users[1].oid)
        self.assertEqual(11, users[2].oid)

    # TODO: Custom assertion method


if __name__ == '__main__':
    unittest.main()
