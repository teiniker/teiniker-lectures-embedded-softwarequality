# REST Service

In this example, we can see how simple a RESTful service can be implemented with
**Flask**.

## Setup 

We start the web service from the command line:
```
$ python3 article_service.py
```

## Access the REST Service

### Find all Articles
```
$ curl -i http://localhost:8080/articles
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
$ curl -i http://localhost:8080/articles/1
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
$ curl -i -X POST localhost:8080/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'
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
$ curl -i -X PUT localhost:8080/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'
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
$ curl -i -X DELETE http://localhost:8080/articles/1
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.2.2 Python/3.9.2
Date: Sat, 31 Dec 2022 12:39:33 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```


## References
* [Python-API-Development-Fundamentals: Lesson01](https://github.com/TrainingByPackt/Python-API-Development-Fundamentals/blob/master/Lesson01/Activity02/basic-api/app.py)

* [Python REST API Tutorial - Building a Flask REST API](https://youtu.be/GMppyAPbLYk?si=xjvZIr3PTYIpQ_Ir)
