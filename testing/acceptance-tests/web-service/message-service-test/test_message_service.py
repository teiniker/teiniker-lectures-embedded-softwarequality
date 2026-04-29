import pytest
from message import Message
from message_service_connector import MessageService


@pytest.fixture
def service():
    return MessageService()


def test_find_by_id(service):
    # Exercise
    msg = service.find_by_id(1124)
    # Verify
    assert msg.address == 1124
    assert msg.priority == 2
    assert msg.data == 'voltage=1.3V'


def test_find_all(service):
    # Exercise
    messages = service.find_all()
    # Verify
    addresses = {msg.address for msg in messages}
    assert 1123 in addresses
    assert 1124 in addresses
    assert 1125 in addresses


def test_insert(service):
    # Exercise
    msg = Message(address=1127, priority=3, data='voltage=5.0V')
    created = service.insert(msg)
    # Verify
    assert created.address == 1127
    assert created.priority == 3
    assert created.data == 'voltage=5.0V'
    service.delete(1127)    # cleanup


def test_update(service):
    # Exercise
    msg = Message(address=1123, priority=1, data='voltage=3.5V')
    updated = service.update(1123, msg)
    # Verify
    assert updated.address == 1123
    assert updated.priority == 1
    assert updated.data == 'voltage=3.5V'


def test_delete(service):
    # Exercise
    msg = Message(address=9999, priority=1, data='test=0.0V')
    service.insert(msg)
    service.delete(9999)
    # Verify
    addresses = {m.address for m in service.find_all()}
    assert 9999 not in addresses
