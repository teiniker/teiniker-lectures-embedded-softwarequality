# Example: Book Service

In this example, we can see how simple a RESTful service can be implemented with
**Flask**.

## Start the Service 

We start the web service from the command line:
```
$ python3 book_service.py
```

## Access the REST Service

### Find all Books
```
$ curl -ik https://localhost:8443/books

HTTP/1.1 401 UNAUTHORIZED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:56:41 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close
```

```
$ curl -ik -u bart:eatmyshorts https://localhost:8443/books

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:57:31 GMT
Content-Type: application/json
Content-Length: 401
Connection: close

{
  "data": [
    {
      "author": "Eric Matthes",
      "id": 1,
      "isbn": "978-1718502703",
      "title": "Python Crash Course"
    },
    {
      "author": "Brett Slatkin",
      "id": 2,
      "isbn": "978-0134853987",
      "title": "Effective Python"
    },
    {
      "author": "Luciano Ramalho",
      "id": 3,
      "isbn": "978-1492056355",
      "title": "Fluent Python"
    }
  ]
}
```

### Find a particular Book
```
$ curl -ik -u bart:eatmyshorts https://localhost:8443/books/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:38:30 GMT
Content-Type: application/json
Content-Length: 104
Connection: close

{
  "author": "Eric Matthes",
  "id": 1,
  "isbn": "978-1718502703",
  "title": "Python Crash Course"
}
```

### Insert a Book
```
$ curl -ik -u bart:eatmyshorts -X POST https://localhost:8443/books -H "Content-Type: application/json" -d '{"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}'

HTTP/1.1 201 CREATED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:38:52 GMT
Content-Type: application/json
Content-Length: 110
Connection: close

{
  "author": "Wes McKinney ",
  "id": 7,
  "isbn": "978-1098104030",
  "title": "Python for Data Analysis"
}
```

### Update a Book
```
$ curl -ik -u bart:eatmyshorts -X PUT https://localhost:8443/books/2 -H "Content-Type: application/json" -d '{"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}'

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:40:20 GMT
Content-Type: application/json
Content-Length: 98
Connection: close

{
  "author": "Brett Slatkin",
  "id": 2,
  "isbn": "0134853989",
  "title": "Effective Python"
}
```

### Delete a Book

```
$ curl -ik -u bart:eatmyshorts -X DELETE https://localhost:8443/books/1

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 10 Jan 2024 11:42:30 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```
