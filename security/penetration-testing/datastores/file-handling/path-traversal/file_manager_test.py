import unittest
from file_manager import FileManager  

class PathTraversalTest(unittest.TestCase):

    def test_read_file(self):
        handler = FileManager()
        txt = handler.read_file("README.txt")
        print(txt)

    # Simulate path-traversal attack
    def test_path_manipulation(self):   
        with self.assertRaises(ValueError):
            handler = FileManager()
            txt = handler.read_file("../file_manager.py")
            print(txt)
            self.fail('This attack worked!')

if __name__ == '__main__':
    unittest.main()
