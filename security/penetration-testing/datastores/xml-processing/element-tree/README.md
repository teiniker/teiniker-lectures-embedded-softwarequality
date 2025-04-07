# Standard Library: xml.etree.ElementTree

The `ElementTree` module is a simple and lightweight XML processor 
module. It provides a simple way to build XML documents and write 
them to files. It also provides a simple way to parse XML documents 
and extract data from them.



## Entity Definitions 

`ElementTree` in Python does not support entity definitions or resolve 
external entities like `DOCTYPE` declarations. It is deliberately designed 
to **avoid parsing DTDs (Document Type Definitions) and external entities** 
to ensure security and simplicity.

This means that if we try to parse XML with entity definitions or references, 
it will typically raise an error or leave the entities unresolved.

The lack of support for entity resolution is intentional:

* It **prevents XML external entity (XXE) attacks**, which are a security 
    vulnerability that can arise when processing external entities in XML.

* It keeps the parser lightweight and simple.




## References

* [Python Standard Library: The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)

* [XML vulnerabilities](https://docs.python.org/3/library/xml.html#xml-vulnerabilities)

*Egon Teiniker, 2020-2024, GPL v3.0*