import unittest

class FileTest(unittest.TestCase):

    def setUp(self):
        # Setup
        self.file = open('Sympathy.txt', 'rt' , encoding="utf-8")

    def tearDown(self):
        # Teardown
        self.file.close()

    def test_read_file(self):
        text = self.file.read()
        print(text)
        self.assertEqual(389, len(text))

    def test_read_lines(self):
        lines = self.file.readlines()
        print(lines)
        self.assertEqual(16, len(lines))

    def test_read_file_autoclose(self):
        with open('Sympathy.txt', 'rt', encoding="utf-8") as file:
            lines = file.readlines()
            print(lines)
            self.assertEqual(16, len(lines))

if __name__ == '__main__':
    unittest.main()
