import unittest
import magic


class FileInspectionTest(unittest.TestCase):
    def test_file_tux(self):
        filepath = 'data/tux'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")

    def test_file_gnu(self):
        filepath = 'data/gnu'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")

    def test_file_document1(self):
        filepath = 'data/document1'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")

    def test_file_document2(self):
        filepath = 'data/document2'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")

    def test_file_numbers(self):
        filepath = 'data/numbers'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")


if __name__ == '__main__':
    unittest.main()
