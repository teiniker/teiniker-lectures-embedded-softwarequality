# HTTP Requests

HTTP is a set of protocols designed to enable communication between clients and servers. It works as a **request-response protocol** between a **client and server**.
A web browser may be the client, and an application on a computer that hosts a website may be the server.

## Setup

The **requests library** is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

To download and install the requests library, use following command:
```
$ pip3 install requests
```

## Requests Library

Requests allows us to send HTTP/1.1 requests extremely easily. 
There’s no need to manually add query strings to your URLs, or to form-encode 
our POST data. Keep-alive and HTTP connection pooling are 100% automatic, 
thanks to urllib3.

_Example_: HTTP GET request 
```Python
    def test_get_request(self):
        # Setup
        url = 'http://localhost:8080/'
        # Exercise
        response = requests.get(url)
        # Verify
        content = response.text
        print(f"Response content: {content}")
        status = response.status_code
        self.assertEqual(200, status)
```

_Example_: HTTP POST request 
```Python
    def test_post_request(self):
        # Setup
        url = 'http://localhost:8080/translator'    
        data = {'word':'cat',
                'language':'Deutsch',
                'action': 'Translate'}
        # Exercise
        response = requests.post(url, data)
        # Verify
        status = response.status_code
        self.assertEqual(200, status)
        content = response.text
        print(f"Response: {response}")
        self.assertTrue('Translate: cat into Katze' in content)
```

## References
* [YouTube (Corey Schafer): Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More](https://youtu.be/tb8gHvYlCFs)
* [YouTube (Corey Schafer): Web Scraping with BeautifulSoup and Requests](https://youtu.be/ng2o98k983k) 

* [Real Python: Python’s Requests Library](https://realpython.com/python-requests/)
* [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
* [GET and POST requests using Python](https://www.geeksforgeeks.org/get-post-requests-using-python/)

*Egon Teiniker, 2020-2022, GPL v3.0*