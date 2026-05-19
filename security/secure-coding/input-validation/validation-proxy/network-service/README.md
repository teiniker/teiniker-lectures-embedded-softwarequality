# Example: ValidationProxy - NetworkService

A Validation Proxy in Python consists of three participants that share a
common interface:

```
NetworkService          (abstract base class, abc.ABC)
    |
    +-- NetworkServiceImpl      (real subject)
    +-- NetworkServiceProxy     (proxy / validation wrapper)
```

Both `NetworkServiceImpl` and `NetworkServiceProxy` inherit from the same
abstract base class. The proxy holds a reference to the real subject and
intercepts every method call to perform validation before delegating.

## Abstract Base Class

The shared interface is defined using `abc.ABC` and `@abstractmethod`:

```python
from abc import ABC, abstractmethod

class NetworkService(ABC):

    @abstractmethod
    def resolve_hostname(self, hostname: str) -> str: 

    @abstractmethod
    def connect(self, address: str, port: int) -> None: 

    @abstractmethod
    def disconnect(self) -> None: 

    @abstractmethod
    def ip_address(self) -> str: 

    @abstractmethod
    def port(self) -> int: 
```

## Real Subject

`NetworkServiceImpl` provides the actual business logic. It maintains a
DNS cache and stores connection state in memory:

```python
class NetworkServiceImpl(NetworkService):

    def __init__(self):
        self._dns_cache = {
            'google.de':           '142.251.36.99',
            'github.com':          '140.82.121.3',
            'ieeexplore.ieee.org': '99.84.91.122',
        }
        self._ip_address: str = ''
        self._port: int = 0

    def resolve_hostname(self, hostname: str) -> str:
        if hostname not in self._dns_cache:
            raise ValueError(f"Hostname not found in DNS cache: '{hostname}'")
        return self._dns_cache[hostname]
    ...
```

## Validation Proxy

`NetworkServiceProxy` implements the same interface and wraps an instance
of `NetworkService`. Every method that accepts external input validates it
first via regex and raises `ValueError` on failure, then delegates to the
wrapped service. Methods with no external input (`disconnect`, `ip_address`,
`port`) are forwarded directly.

```python
import re
import unicodedata
from network_service import NetworkService

HOSTNAME_REGEX = r'^([a-zA-Z0-9\-]{1,63}\.)+[a-zA-Z]{2,63}$'
IPV4_REGEX     = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'

class NetworkServiceProxy(NetworkService):

    def __init__(self, service: NetworkService):
        self._service = service

    def resolve_hostname(self, hostname: str) -> str:
        normalized = unicodedata.normalize("NFKC", hostname)
        if not re.match(HOSTNAME_REGEX, normalized):
            raise ValueError(f"Invalid hostname format: '{hostname}'")
        return self._service.resolve_hostname(hostname)

    def connect(self, address: str, port: int) -> None:
        normalized = unicodedata.normalize("NFKC", address)
        if not re.match(IPV4_REGEX, normalized):
            raise ValueError(f"Invalid IP address format: '{address}'")
        if port == 0 or port > 65535:
            raise ValueError(f"Port number out of range: {port}")
        self._service.connect(address, port)

    def disconnect(self) -> None:
        self._service.disconnect()
    ...
```

Input strings are normalized with `unicodedata.normalize("NFKC", ...)` before
matching to prevent Unicode lookalike bypass attacks.

## Usage

The proxy is transparent to the caller - it is used exactly like the real
service because both implement the same interface:

```python
from network_service import NetworkServiceImpl
from network_service_proxy import NetworkServiceProxy

service = NetworkServiceProxy(NetworkServiceImpl())

ip = service.resolve_hostname('github.com')   # '140.82.121.3'
service.connect(ip, 443)
print(service.ip_address(), service.port())   # 140.82.121.3  443
service.disconnect()

service.resolve_hostname('bad host!')         # raises ValueError
service.connect('192.168.1.1', 0)            # raises ValueError
```

*Egon Teiniker, 2020-2026, GPL v3.0*
