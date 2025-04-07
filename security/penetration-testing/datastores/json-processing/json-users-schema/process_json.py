import unittest
import json
from jsonschema import validate, ValidationError, SchemaError

class JsonTest(unittest.TestCase):
    def schema_validation(self, json_filename, schema_filename):
        # Parse XML and XSD files
        with open(json_filename, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)        
        with open(schema_filename, "r", encoding="utf-8") as schema_file:
            schema = json.load(schema_file)
        validate(instance=data, schema=schema)


    def test_read_valid_json(self):
        self.schema_validation("users.json", "users-schema.json")

    def test_read_invalid_type(self):
        with self.assertRaises(ValidationError) as e:
            self.schema_validation("users-invalid-type.json", "users-schema.json")
        self.assertEqual("'2' is not of type 'integer'", str(e.exception.message))

    def test_read_too_many_properties(self):
        with self.assertRaises(ValidationError) as e:
            self.schema_validation("users-too-many-properties.json", "users-schema.json")
        self.assertEqual("Additional properties are not allowed ('role' was unexpected)", str(e.exception.message))


if __name__ == '__main__':
    unittest.main()