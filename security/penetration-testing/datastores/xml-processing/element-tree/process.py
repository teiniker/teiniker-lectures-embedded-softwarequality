import unittest
import xml.etree.ElementTree as et 

class ElementTreeTest(unittest.TestCase):

    def test_read_xml(self):
        tree = et.parse("users.xml") 
        root = tree.getroot()
        print(root.tag)

    def test_read_xml_with_entity(self):
        with self.assertRaises(et.ParseError):
            et.parse("users-entity-file.xml") 

if __name__ == '__main__':
    unittest.main()