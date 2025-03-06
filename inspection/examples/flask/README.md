# Example: Analyze Flask

The following examples will analyze the **Flak web framework**.

## Clone Flask

```
$ git clone https://github.com/pallets/flask.git
```


## Software Metrics

_Example:_ Lines of Code (LOC)
```
$ radon raw src/
src/flask/signals.py
    LOC: 17
    LLOC: 13
    SLOC: 13
    Comments: 1
    Single comments: 1
    Multi: 0
    Blank: 3
    - Comment Stats
        (C % L): 6%
        (C % S): 8%
        (C + M % L): 6%
...
```

_Example:_ Cyclomatic Complexity Number (CCN)
```
$ radon cc src/ -s
src/flask/app.py
    M 1082:4 Flask.make_response - C (16)
    M 499:4 Flask.run - C (12)
    M 956:4 Flask.url_for - C (12)
    M 1223:4 Flask.preprocess_request - B (8)
    M 732:4 Flask.handle_user_exception - B (7)
    M 764:4 Flask.handle_exception - B (6)
    M 1250:4 Flask.process_response - B (6)
    M 1431:4 Flask.wsgi_app - B (6)
    C 79:0 Flask - A (5)
    M 391:4 Flask.create_url_adapter - A (5)
    M 431:4 Flask.raise_routing_exception - A (5)
    M 459:4 Flask.update_template_context - A (5)
    M 1278:4 Flask.do_teardown_request - A (5)
    M 351:4 Flask.create_jinja_environment - A (4)
    M 697:4 Flask.handle_http_exception - A (4)
    M 832:4 Flask.dispatch_request - A (4)
...
```


## Static Code Analysis

_Example:_ Reporting code smells using PyLint

```
$ pylint src/
************* Module flask.sessions
src/flask/sessions.py:108:0: C0301: Line too long (112/100) (line-too-long)
src/flask/sessions.py:205:0: C0301: Line too long (113/100) (line-too-long)
src/flask/sessions.py:23:1: W0511: TODO generic when Python > 3.8 (fixme)
src/flask/sessions.py:52:1: W0511: TODO generic when Python > 3.8 (fixme)
src/flask/sessions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
...
```

PyLint is comprehensive and focuses on code quality and enforcement
of Python coding standards according to **PEP 8**, in addition to
**detecting errors**.
It offers highly detailed reports on **code smells**, suggests
refactorings, and checks for a wide range of programming standards.


_Example_: Reporting problems unsing Flake8
```
$ flake8 src/
src/flask/__init__.py:5:1: F401 '.json' imported but unused
src/flask/__init__.py:6:1: F401 '.app.Flask' imported but unused
src/flask/__init__.py:7:1: F401 '.blueprints.Blueprint' imported but unused
src/flask/__init__.py:8:1: F401 '.config.Config' imported but unused
...
src/flask/app.py:67:80: E501 line too long (83 > 79 characters)
src/flask/app.py:68:80: E501 line too long (83 > 79 characters)
src/flask/app.py:88:80: E501 line too long (83 > 79 characters)
src/flask/app.py:110:80: E501 line too long (84 > 79 characters)
...
```

_Example:_ Using type hints (src/flask/app.py)
```Python
    def __init__(
        self,
        import_name: str,
        static_url_path: str | None = None,
        static_folder: str | os.PathLike[str] | None = "static",
        static_host: str | None = None,
        host_matching: bool = False,
        subdomain_matching: bool = False,
        template_folder: str | os.PathLike[str] | None = "templates",
        instance_path: str | None = None,
        instance_relative_config: bool = False,
        root_path: str | None = None,
    ):
    #...


    def get_send_file_max_age(self, filename: str | None) -> int | None:
    #...

    def send_static_file(self, filename: str) -> Response:
    #...
```



*Egon Teiniker, 2020-2024, GPL v3.0*
