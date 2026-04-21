# Start and Stop a Web Service for Acceptance Tests

We can start the Flask server for each test by launching it in the `setup_method()` 
method and terminating it in the `teardown_method()` method of our test class. 

This approach ensures **each test has a clean server state** but comes with 
**performance trade-offs** (since starting and stopping the server can be 
relatively slow).

_Example:_ Start and stop a Flask web service for each test 

```Python
from book_service import app

def run_app():
    app.run(port=8080, debug=True, use_reloader=False)

def wait_for_server(host, port, timeout=5.0):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (ConnectionRefusedError, OSError):
            time.sleep(0.1)
    raise SystemError(f"Server at {host}:{port} did not start in time.")


class TestBookService:

    def setup_method(self):
        self.base_url = 'http://localhost:8080/books'
        self.session = requests.Session()
        self.server = multiprocessing.Process(target=run_app)
        self.server.start()
        wait_for_server('localhost', 8080)

    def teardown_method(self):
        self.server.terminate()
        self.server.join()
        self.session.close()
    # ...
```

We import the Flask app from `book_service.py` and define a function
`run_app()` that starts the server. 

In the `setup_method()`, we create a new process to run the app, start it, 
and wait a moment for it to be ready.

In the `teardown_method()` method, we terminate the server process and wait for 
it to finish.

* **debug=False** and **use_reloader=False** are critical to avoid spawning 
multiple unnecessary processes.

* **time.sleep()** provides time for the server to start. We could replace 
this with a retry loop checking for the port to open, for robustness.

* **self.server.terminate()** cleanly stops the process, and **join()** 
ensures it's finished.

* **wait_for_server()** tries to open a socket connection repeatedly until 
the Flask server is listening, up to a max of 5 seconds.
This is faster and safer than a fixed `sleep()` because it doesn't waste 
time once the server is ready.
It also avoids the flakiness of assuming the server is up after a specific 
amount of time.

*Egon Teiniker, 2020-2026, GPL v3.0*
