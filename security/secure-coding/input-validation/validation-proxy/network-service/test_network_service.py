import pytest
from network_service import NetworkServiceImpl
from network_service_proxy import NetworkServiceProxy


def create_network_service():
    return NetworkServiceProxy(NetworkServiceImpl())


def test_resolve_hostname_valid():
    proxy = create_network_service()
    assert proxy.resolve_hostname('google.de') == '142.251.36.99'
    assert proxy.resolve_hostname('github.com') == '140.82.121.3'
    assert proxy.resolve_hostname('ieeexplore.ieee.org') == '99.84.91.122'


def test_resolve_hostname_not_in_cache():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.resolve_hostname('unknown.example.com')


def test_resolve_hostname_invalid_format():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.resolve_hostname('invalid_host')

def test_resolve_hostname_no_tld():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.resolve_hostname('no-tld')

def test_resolve_hostname_empty():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.resolve_hostname('')


def test_connect_valid():
    proxy = create_network_service()
    proxy.connect('192.168.1.1', 8080)
    assert proxy.ip_address() == '192.168.1.1'
    assert proxy.port() == 8080


def test_connect_and_disconnect():
    proxy = create_network_service()
    proxy.connect('10.0.0.1', 443)
    proxy.disconnect()
    assert proxy.ip_address() == ''
    assert proxy.port() == 0


def test_connect_invalid_address_not_ip():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.connect('not-an-ip', 80)

def test_connect_invalid_address_incomplete():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.connect('192.168.1', 80)

def test_connect_invalid_address_too_many_octets():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.connect('192.168.1.1.1', 80)


def test_connect_invalid_port_zero():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.connect('192.168.1.1', 0)

def test_connect_invalid_port_exceeds_maximum():
    proxy = create_network_service()
    with pytest.raises(ValueError):
        proxy.connect('192.168.1.1', 65536)


def test_connect_minimum_port():
    proxy = create_network_service()
    proxy.connect('192.168.1.1', 1)
    assert proxy.port() == 1

def test_connect_maximum_port():
    proxy = create_network_service()
    proxy.connect('192.168.1.1', 65535)
    assert proxy.port() == 65535
