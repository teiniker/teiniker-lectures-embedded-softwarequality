import unittest
from user_table import UserTable, User 
from user_table_builder import UserTableBuilder

class UserTableTest(unittest.TestCase):
    def setUp(self):
        self.user_table = UserTable()
        self.user_table = (UserTableBuilder()
                           .user(3,"Lisa","lKi8/hhgT")
                           .user(7,"Bart","kJ7&fRsd34%7")
                           .build())

    def test_find_by_id(self):
        actual = self.user_table.find_by_id(3)
        expected = User(3,"Lisa","lKi8/hhgT")
        self.assertEqual(expected, actual)

    def test_find_all(self):
        users = self.user_table.find_all()
        self.assertEqual(len(users), 2)
        self.assertIn(3, users[0].oid)
        self.assertIn(7, users[1].oid)

    def test_insert_user(self):
        user = User(3,"Homer","lKfDt54sss6")
        self.user_table.insert(user)
        self.assertEqual(len(self.user_table.find_all()), 3)
        self.assertIn(user, self.user_table.find_all())

    # Helper method
    def assertEqualUser(self, expected:User, actual:User):
        self.assertEqual(expected.oid, actual.oid)
        self.assertEqual(expected.username, actual.username)
        self.assertEqual(expected.password, actual.password)

if __name__ == '__main__':
    unittest.main()
