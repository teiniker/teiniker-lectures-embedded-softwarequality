# Beautiful Soup 

Beautiful Soup is a library that makes it easy to scrape information from web pages. 
It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching,
and modifying the parse tree.

* Parses poorly-formed HTML (e.g., missing tags)

* Supports multiple parsers: built-in (html.parser), lxml, or html5lib

* Allows easy navigation using tags, attributes, and CSS selectors

* Can search, filter, and modify HTML/XML trees



## Setup 

Beautiful Soup is a Python library and can be installed using pip:

```bash 
$ pip3 install beautifulsoup4
```

## Parsing HTML Content

Beautiful Soup can parse HTML content using the following methods:

| Method                  | Description                                  |
| ----------------------- | -------------------------------------------- |
| `soup.find(tag)`        | Finds the **first** tag                      |
| `soup.find_all(tag)`    | Finds **all** tags of that type              |
| `soup.get_text()`       | Extracts all text content                    |
| `tag['attribute']`      | Gets a tag’s attribute (e.g., `href`, `src`) |
| `soup.select(selector)` | CSS-style selector search                    |


_Example:_ Parsing GET response 
```HTML
<html>
<head>
    <title>Servlet Translator</title>
</head>
<body>
<h2>Translator </h2>
<form method="POST" action="translator" >
    <table border="0" >
        <colgroup>
            <col width="100"> <col width="100">
        </colgroup>
        <tr>
            <th align="left">
                Word:
            </th>
            <th align="left">
                <input type="text" name="word" maxlength="30" size="20"> <br>
            </th>
        </tr>
        ...
```

Running the HTML string through Beautiful Soup gives us a **BeautifulSoup object**, 
which represents the document as a **nested data structure**.

```python
soup = BeautifulSoup(html_content, 'html.parser')
    
title = soup.title.string.strip()
self.assertEqual(title, "Servlet Translator")
    
form = soup.find('form')
self.assertEqual(form.get('method'), 'POST')
self.assertEqual(form.get('action'), 'translator')

input_word = soup.find('input', {'name': 'word'})
self.assertIsNotNone(input_word)
self.assertEqual(input_word.get('type'), 'text')
self.assertEqual(input_word.get('maxlength'), '30')
self.assertEqual(input_word.get('size'), '20')
```



## References

* [YouTube (Corey Schafer): Web Scraping with BeautifulSoup and Requests](https://youtu.be/ng2o98k983k?si=UOjAyahrlk9SqAAH)

* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

*Egon Teiniker, 2020-2025, GPL v3.0*