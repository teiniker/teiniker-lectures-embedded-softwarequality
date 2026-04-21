import time
import socket
import multiprocessing
import requests

from book_service import app

def run_app():
    app.run(port=8080, debug=False, use_reloader=False)

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

    def test_find_by_id(self):
        response = self.session.get(f'{self.base_url}/1', timeout=5)
        assert response.status_code == 200
        assert response.headers['content-type'] == 'application/json'
        json_data = response.json()
        assert json_data['id'] == 1
        assert json_data['author'] == 'Eric Matthes'
        assert json_data['isbn'] == '978-1718502703'
        assert json_data['title'] == 'Python Crash Course'

    def test_find_all(self):
        response = self.session.get(self.base_url, timeout=5)
        assert response.status_code == 200
        assert response.headers['content-type'] == 'application/json'
        ids = [book['id'] for book in response.json()['data']]
        assert ids[0] == 1
        assert ids[1] == 2
        assert ids[2] == 3

    def test_insert(self):
        payload = {"id": 7, "author": "Wes McKinney ", "title": "Python for Data Analysis", "isbn": "978-1098104030"}
        response = self.session.post(self.base_url, timeout=5, json=payload)
        assert response.status_code == 201

    def test_update(self):
        payload = {"author": "Brett Slatkin", "title": "Effective Python", "isbn": "0134853989"}
        response = self.session.put(f'{self.base_url}/2', timeout=1, json=payload)
        assert response.status_code == 200

    def test_delete(self):
        response = self.session.delete(f'{self.base_url}/2', timeout=1)
        assert response.status_code == 204
