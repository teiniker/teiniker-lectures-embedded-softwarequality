# Basic Authentication

In this example, we can see how simple a RESTful service can be implemented with
**Flask**.

## Setup 
```
$ pip3 install Flask-HTTPAuth
```

We start the web service from the command line:
```
$ python3 article_service.py
```

## Flask-HTTPAuth

Flask-HTTPAuth is a Flask extension that simplifies the use of HTTP authentication with Flask routes.

The function decorated with the `verify_password` decorator receives the username and password sent by the client. If the credentials belong to a user, then the function should return the user object. If the credentials are invalid the function can return `None` or `False`. The user object can then be queried from the `current_user()` method of the authentication instance.


## Access the REST Service

### Find all Articles
```
$ curl -i -k https://localhost:8443/articles
HTTP/1.1 401 UNAUTHORIZED
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Thu, 12 Jan 2023 14:33:18 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close
```

```
$ curl -i -k -u student:student https://localhost:8443/articles
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:13:49 GMT
Content-Type: application/json
Content-Length: 286
Connection: close

{
  "data": [
    {
      "description": "Effective Python",
      "id": 1,
      "price": 2390
    },
    {
      "description": "Effective Python",
      "id": 2,
      "price": 2390
    },
    {
      "description": "Effective Python",
      "id": 3,
      "price": 2390
    }
  ]
}
```

### Find a particular Article
```
$ curl -i -k -u student:student https://localhost:8443/articles/1
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:14:13 GMT
Content-Type: application/json
Content-Length: 68
Connection: close

{
  "description": "Effective Python",
  "id": 1,
  "price": 2390
}
```

### Insert an Article
```
$ curl -i -k -u student:student -X POST https://localhost:8443/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'
HTTP/1.1 201 CREATED
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:16:59 GMT
Content-Type: application/json
Content-Length: 67
Connection: close

{
  "description": "Learning Python",
  "id": 7,
  "price": 5448
}
```

### Update an Article
```
$ curl -i -k -u student:student -X PUT https://localhost:8443/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:32:29 GMT
Content-Type: application/json
Content-Length: 72
Connection: close

{
  "description": "Clean Code in Python",
  "id": 2,
  "price": 3700
}
```

### Delete an Article

```
$ curl -i -k -u student:student -X DELETE https://localhost:8443/articles/1
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:39:33 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```


## References
* [Python-API-Development-Fundamentals: Lesson01](https://github.com/TrainingByPackt/Python-API-Development-Fundamentals/blob/master/Lesson01/Activity02/basic-api/app.py)

* [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

*Egon Teiniker, 2020-2023, GPL v3.0*