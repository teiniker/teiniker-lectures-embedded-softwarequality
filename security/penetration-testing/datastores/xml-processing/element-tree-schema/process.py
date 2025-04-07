import unittest
from lxml import etree

class ElementTreeTest(unittest.TestCase):

    def schema_validation(self, xml_file, xsd_file):
        # Parse XML and XSD files
        with open(xsd_file, 'r') as schema_file:
            schema_root = etree.XML(bytes(schema_file.read(), "utf-8"))
            schema = etree.XMLSchema(schema_root)

        with open(xml_file, 'r') as xml_file:
            xml_doc = etree.parse(xml_file)

        # Validate XML against the schema
        return schema.validate(xml_doc)

    def test_valid_xml(self):
        is_valid = self.schema_validation("users.xml", "users.xsd")
        self.assertTrue(is_valid)

    def test_invalid_order(self):
        is_valid =  self.schema_validation("users-invalid-order.xml", "users.xsd")    
        self.assertFalse(is_valid)

    def test_missing_id(self):
        is_valid =  self.schema_validation("users-missing-id.xml", "users.xsd")    
        self.assertFalse(is_valid)

    def test_element_injection(self):
        is_valid =  self.schema_validation("users-element-injection.xml", "users.xsd")    
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()