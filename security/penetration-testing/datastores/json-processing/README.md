# JSON Processing

## JSON Format 

**JSON (JavaScript Object Notation)** is a lightweight, text-based 
**data interchange format** often used for transmitting data between 
a server and a client in web applications. Although derived from 
JavaScript, it is language-independent and can be used in virtually 
any modern programming language.

Here’s an overview of JSON’s main characteristics:

* **Basic Structure**  
   - A **JSON object** is enclosed in curly braces `{ ... }` and 
    contains one or more key-value pairs.  
   - A **JSON array** is enclosed in square brackets `[ ... ]` and 
    contains a list of items.  
   - **Keys** in a JSON object must always be strings (wrapped in 
    double quotes).  
   - **Values** can be:
     - A **string** (in double quotes)
     - A **number** (integer or floating-point)
     - A **boolean** (`true` or `false`)
     - **null**
     - Another **JSON object**
     - A **JSON array**

   ```json
   {
     "name": "Homer",
     "age": 39,
     "isMarried": true,
     "children": ["Bart", "Lisa", "Maggie"],
     "address": {
       "street": "742 Evergreen Terrace",
       "city": "Springfield"
     }
   }
   ```

* **Syntax Rules**  
   - Keys **must be** in double quotes.  
   - Strings **must be** in double quotes.  
   - No trailing commas are allowed.  
   - Whitespace (spaces, tabs, newlines) is optional and typically 
    used for readability.

* **Common Uses**  
   - **APIs**: Web services often send requests and responses in JSON format.  
   - **Configuration Files**: Many systems and tools use JSON for storing settings.  
   - **Data Storage**: Some databases (like document-based NoSQL databases) store records in JSON or JSON-like formats.


JSON is a simple, flexible, and widely supported format for encoding structured 
data, making it an industry standard for data exchange in web applications and 
beyond.


## Parsing JSON in Python

In Python, the built-in **json** module provides a straightforward way to 
parse (deserialize) JSON data from a string or file into Python objects 
such as dictionaries, lists, etc. 

It also allows you to generate (serialize) JSON strings from Python objects.

## Parsing JSON  

_Example:_ Parsing a JSON string into a Python dictionary.
```python
import json

json_string = '{"name": "Marge", "age": 36, "isMarried": true}'
python_data = json.loads(json_string)

print(python_data)
# Output: {'name': 'Marge', 'age': 36, 'isMarried': True}

# Accessing the data
print(python_data['name'])  # Output: Marge
print(python_data['age'])   # Output: 36
```

_Example:_ Parsing a JSON file into a Python dictionary.
```python
import json

with open('data.json', 'r') as file:
    python_data = json.load(file)

print(python_data)
# Output might be a dictionary or list, depending on the JSON structure.
```


## Validating JSON

We can use the **jsonschema** library to validate JSON data against a schema.

### Setup 

```bash
$ pip3 install jsonschema
```

### Creating a JSON Schema

A JSON Schema is itself a JSON document that describes the structure and 
constraints of the data you want to validate.

_Example:_ A simple JSON schema for validating a list of users
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Users Schema",
  "type": "object",
  "properties": {
    "users": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": { "type": "integer" },
          "username": { "type": "string" },
          "password": { "type": "string" }
        },
        "required": ["id", "username", "password"]
      }
    }
  },
  "required": ["users"],
  "additionalProperties": false
}
```

Elements of a Schema:
* **type**: Specifies whether the data should be an `object`, 
    `array`, `string`, `number`, etc.
* **properties**: Defines the expected fields for an `object`.
* **required**: Lists the properties that must be present.
* **additionalProperties**: Controls whether properties not listed 
    under properties are allowed.
* **items**: Describes the structure of elements within an array.

### Validate JSON Data

We load both the schema and the data and then call `validate()`.

_Example:_ Validating JSON data against a schema.
```python
import json
from jsonschema import validate, ValidationError, SchemaError

def main():
    # Load JSON data
    with open("users.json", "r") as json_file:
        data = json.load(json_file)

    # Load JSON Schema
    with open("users-schema.json", "r") as schema_file:
        schema = json.load(schema_file)

    # Validate the data against the schema
    try:
        validate(instance=data, schema=schema)
        print("JSON is valid against the schema!")
    except ValidationError as e:
        print("JSON validation error!")
        print(f"Error message: {e.message}")
    except SchemaError as e:
        print("JSON schema error!")
        print(f"Error message: {e.message}")
```

The jsonschema library throws two main exceptions you may want to handle:

* **ValidationError**: Thrown when the data does not conform to the schema.
* **SchemaError**: Thrown when the schema itself is invalid or references 
    something incorrectly.

## Examples and Exercises

* JSON Parsing 
  * Example: [json-users](json-users/)

* JSON Validation
    * Example: [json-users-schema](json-users-schema/)     


## References

* [The Python Standard Library: json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)

* [JSON Schema](https://json-schema.org/)

* [GitHub: jsonschema](https://github.com/python-jsonschema/jsonschema)


*Egon Teiniker, 2020-2025, GPL v3.0*