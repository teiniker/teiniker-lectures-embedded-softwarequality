from abc import ABC, abstractmethod


class NetworkService(ABC):
    """Abstract base class defining the NetworkService interface."""

    @abstractmethod
    def resolve_hostname(self, hostname: str) -> str:
        """Resolve a hostname to an IP address string."""

    @abstractmethod
    def connect(self, address: str, port: int) -> None:
        """Establish a connection to the given IP address and port."""

    @abstractmethod
    def disconnect(self) -> None:
        """Close the current connection."""

    @abstractmethod
    def ip_address(self) -> str:
        """Return the IP address of the current connection."""

    @abstractmethod
    def port(self) -> int:
        """Return the port number of the current connection."""


class NetworkServiceImpl(NetworkService):
    """Concrete implementation of NetworkService.

    Uses a DNS cache for hostname resolution and stores
    connection state in memory.
    """
    _dns_cache: dict[str, str]
    _ip_address: str
    _port: int

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

    def connect(self, address: str, port: int) -> None:
        self._ip_address = address
        self._port = port

    def disconnect(self) -> None:
        self._ip_address = ''
        self._port = 0

    def ip_address(self) -> str:
        return self._ip_address

    def port(self) -> int:
        return self._port
