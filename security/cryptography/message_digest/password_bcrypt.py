import unittest
import bcrypt

class BCryptTest(unittest.TestCase):

    def test_bcrypt(self):
        passwd = b's$cret12'
        # randomly generated salt
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(passwd, salt)
        print(hashed)

        if bcrypt.checkpw(passwd, hashed):
            print("valid password")
        else:
            print("password rejected")


if __name__ == '__main__':
    unittest.main()
