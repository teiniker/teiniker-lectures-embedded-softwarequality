# XML Schema Validation 

## Setup 

We use the lxml library to validate the XML file against the schema.
    
```bash
$ pip install lxml
```

## XML Schema Definitions 

The given XML Schema `users.xsd` defines the structure of an XML document 
that represents a collection of users.

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="users">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="user" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="username" type="xs:string" />
                            <xs:element name="password" type="xs:string" />
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:integer" use="required" />
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
```

* **Schema Declaration**: `<xs:schema>`: Root element of the XML Schema document. 
    It declares the XML Schema namespace, which provides standard types like 
    `xs:string` and `xs:integer`.

* **Root Element**: 
    * `<xs:element name="users">`: The root element of the XML document is named `users`.
    * `<xs:complexType>`: The root element has a complex type, which means it can contain 
        other elements.
    * `<xs:sequence>`: The child elements of the root element must appear in the order 
        specified by the sequence.

* **Child Element**:
    * `<xs:element name="user" maxOccurs="unbounded">`: 
        * The `users` element contains multiple `user` elements.
        * `maxOccurs="unbounded"`: The `user` element can appear multiple times.
        * `<xs:complexType>`: The `user` element has a complex type, which means it can contain
            other elements.
        * `<xs:sequence>`: The child elements of the `user` element must appear in the order
            specified by the sequence.
        * `<xs:element name="username" type="xs:string" />`: The `user` element contains a
            `username` element of type `xs:string`.
        * `<xs:element name="password" type="xs:string" />`: The `user` element contains a
            `password` element of type `xs:string`.
    * `<xs:attribute>`:
        * `name="id"`: Declares the id attribute for `<user>`.
        * `type="xs:integer"`: Specifies that the id attribute must be an integer.
        * `use="required"`: Makes the id attribute mandatory.

This schema enforces both structural and data type constraints for the XML document, 
ensuring that it meets the specified format and rules.


## References

* [XML Schema Tutorial](https://www.w3schools.com/xml/schema_intro.asp)

*Egon Teiniker, 2020-2024, GPL v3.0*