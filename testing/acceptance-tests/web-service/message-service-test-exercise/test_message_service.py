import pytest
from message import Message
from message_service_connector import MessageService


@pytest.fixture
def service():
    return MessageService()

# TODO: Implement the test cases for the MessageService methods
