# Example: Message Service

## Setup

```bash
$ python message_service.py
```

## Access Message Service Using curl

### Find all Messages

```bash
$ curl -i http://localhost:8080/messages 

HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.13.5
Date: Wed, 29 Apr 2026 05:39:50 GMT
Content-Type: application/json
Content-Length: 278
Connection: close

{
  "data": [
    {
      "address": 1123,
      "data": "voltage=3.4V",
      "priority": 2
    },
    {
      "address": 1124,
      "data": "voltage=1.3V",
      "priority": 2
    },
    {
      "address": 1125,
      "data": "voltage=-1.7V",
      "priority": 1
    }
  ]
}
```

### Find a particular Message

```bash
$ curl -i http://localhost:8080/messages/1124

HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.13.5
Date: Wed, 29 Apr 2026 06:04:15 GMT
Content-Type: application/json
Content-Length: 65
Connection: close

{
  "address": 1124,
  "data": "voltage=1.3V",
  "priority": 2
}
```

### Insert a Message

```bash
$ curl -i -X POST localhost:8080/messages -H "Content-Type: application/json" -d '{"address": 1127, "priority": 3, "data":"voltage=5.0V"}'

HTTP/1.1 201 CREATED
Server: Werkzeug/3.1.8 Python/3.13.5
Date: Wed, 29 Apr 2026 06:04:41 GMT
Content-Type: application/json
Content-Length: 65
Connection: close

{
  "address": 1127,
  "data": "voltage=5.0V",
  "priority": 3
}
```

### Update a Message

```bash
$ curl -i -X PUT localhost:8080/messages/1124 -H "Content-Type: application/json" -d '{"address": 1124, "priority": 9, "data":"voltage=1.0V"}'

HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.13.5
Date: Wed, 29 Apr 2026 06:07:25 GMT
Content-Type: application/json
Content-Length: 65
Connection: close

{
  "address": 1124,
  "data": "voltage=1.0V",
  "priority": 9
}
```

### Delete a Message

```bash
$ curl -i -X DELETE http://localhost:8080/messages/1124

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/3.1.8 Python/3.13.5
Date: Wed, 29 Apr 2026 06:07:56 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```

*Egon Teiniker, 2020-2026, GPL v3.0*
