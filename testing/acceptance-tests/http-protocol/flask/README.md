# Flask

Flask is a web application framework written in Python and represents a collection of libraries 
and modules that enables a web application developer to write applications without having to 
bother about low-level details such as protocols, thread management etc.

## Setup

Install and update using `pip3`:

```
$ pip3 install Flask
```


## Introduction 

Flask is based on the following components:

* **Web Server Gateway Interface (WSGI)** has been adopted as a standard for Python web application 
    development. WSGI is a specification for a universal interface between the web server and the 
    web applications.

* **Werkzeug** is a WSGI toolkit, which implements requests, response objects, and other utility 
    functions. This enables building a web framework on top of it. 
    The Flask framework uses Werkzeug as one of its bases.

* **Jinja2** is a popular templating engine for Python. 
    A web templating system combines a template with a certain data source to render dynamic web pages.

Flask does not have built-in abstraction layer for database handling, nor does it have form a 
validation support. Instead, Flask supports the **extensions** to add such functionality to the application. 


## HTTP methods

The HTTP protocol is the foundation of data communication in world wide web. 
Different methods of data retrieval from specified URL are defined in this protocol.

* **GET** Sends data in unencrypted form to the server. Most common method to retrieve web pages.

* **HEAD** Same as GET, but without response body.

* **POST** Used to send HTML form data to server. Data received by POST method is not cached by server.

* **PUT** Replaces all current representations of the target resource with the uploaded content.

* **DELETE** Removes all current representations of the target resource given by a URL.

By default, the Flask route responds to the GET requests. 
However, this preference can be altered by providing methods argument to route() decorator.


## Request Object

The data from a client’s web page is sent to the server as a global request object. 
In order to process the request data, it should be imported from the Flask module.

Important attributes of request object are:

* **Form** It is a dictionary object containing key and value pairs of form parameters and their values.

* **args** Parsed contents of query string which is part of URL after question mark (?).

* **Cookies**  Dictionary object holding Cookie names and values.

* **files** Data pertaining to uploaded file.

* **method** Current request method.


## Templates
Generating HTML content from Python code is cumbersome, especially when variable data and Python language 
elements like conditionals or loops need to be put. 

This is where one can take advantage of **Jinja2 template engine**, on which Flask is based. 
Instead of returning hardcode HTML from the function, a HTML file can be rendered by the 
render_template() function.

Flask will try to find the HTML file in the templates folder:
```
├── templates
│   └── hello.html
└── web_app.py
```

The jinja2 template engine uses the following delimiters for escaping from HTML.

* `{% ... %}` for Statements
* `{{ ... }}` for Expressions to print to the template output
* `{# ... #}` for Comments not included in the template output
* `# ... ##` for Line Statements


## Static Files

A web application often requires a static file such as a javascript file or a CSS file 
supporting the display of a web page. 
These files are served from static folder in our package or next to our module and it will 
be available at `/static` on the application

A special endpoint `static` is used to generate URL for static files.



## References
* [Flask's Documentation](https://flask.palletsprojects.com/en/2.0.x/)

* [Flask Tutorial](https://www.tutorialspoint.com/flask/index.htm)

* [Youtube (Schafer): Python Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)