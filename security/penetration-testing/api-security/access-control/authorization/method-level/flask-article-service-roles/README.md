# Example: Method-Level Authorization - Article Service

In this example, we can see how simple a RESTful service can be implemented 
with **Flask** using **Basic Authentication** and **Role-Based Authorization**
on HTTP method level.

## Setup 
```
$ pip3 install Flask-HTTPAuth
```

We start the web service from the command line:
```
$ python3 article_service.py
```

## Implementation Details

The following code snippets show the implementation of Role-Based Authorization 
at the method level within the Flask web server.

* **User and Role Management**:

  ```Python
  users = 
  {
      "student": generate_password_hash("student"),
      "homer": generate_password_hash("duffbeer"),
      "burns": generate_password_hash("money")
  }

  roles = 
  {
      "burns": ["admin", "user"],
      "homer": ["user"],
      "student": ["user"]
  }
  ```

  * `users` is a dictionary that stores usernames and hashed passwords.
      `generate_password_hash` hashes passwords for secure storage (not 
      storing plaintext passwords). 
  
  * `roles` defines the roles associated with each user.
    For example, `burns` has both `admin` and `user` roles, while `homer` 
    and `student` only have the user role.

* **Role Retrieval**:

  ```Python
  @auth.get_user_roles
  def get_user_roles(user):
      return roles.get(user)
  ```

  * This function retrieves the roles of the authenticated user from the 
    roles dictionary.

* **Protected Route**:

  ```Python
  @app.route('/articles', methods=['GET'])
  @auth.login_required(role="admin")
  def find_all():
      return jsonify({'data': table}), HTTPStatus.OK
  ```
  * **Route**: `/articles` is a GET endpoint.

  * **Decorator**: `@auth.login_required(role="admin")` requires authentication.
    Only users with the `admin` role can access this route.


## Access REST Service via cURL

### Find all Articles

```
$ curl -i -k -u homer:duffbeer https://localhost:8443/articles

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:18:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money https://localhost:8443/articles

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 09:56:44 GMT
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
$ curl -i -k -u homer:duffbeer https://localhost:8443/articles/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 09:58:02 GMT
Content-Type: application/json
Content-Length: 68
Connection: close

{
  "description": "Effective Python",
  "id": 1,
  "price": 2390
}
```

```
$ curl -i -k -u burns:money https://localhost:8443/articles/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:20:04 GMT
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
$ curl -i -k -u homer:duffbeer -X POST https://localhost:8443/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:22:01 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X POST https://localhost:8443/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'

HTTP/1.1 201 CREATED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:22:47 GMT
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
$ curl -i -k -u homer:duffbeer -X PUT https://localhost:8443/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:25:58 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X PUT https://localhost:8443/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:26:45 GMT
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
$ curl -i -k -u homer:duffbeer -X DELETE https://localhost:8443/articles/1

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:27:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X DELETE https://localhost:8443/articles/1

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:28:44 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```