import os
import sqlite3
from message import Message
from message_service_connector import MessageService

DB_PATH = os.path.join(os.path.dirname(__file__),'..', 'message-service', 'message.db')

def execute_sql_script(filename: str) -> None:
    """Execute a SQL script from a file against the message database."""
    script_path = os.path.join(os.path.dirname(__file__), filename)
    with open(script_path, 'r', encoding='utf-8') as sql_file:
        with sqlite3.connect(DB_PATH) as conn:
            conn.cursor().executescript(sql_file.read())


class TestMessageService:

    def setup_method(self):
        execute_sql_script('sql/setup.sql')
        self.service = MessageService()

    def teardown_method(self):
        execute_sql_script('sql/teardown.sql')

    def test_find_by_id(self):
        # Exercise
        msg = self.service.find_by_id(1124)
        # Verify
        assert msg.address == 1124
        assert msg.priority == 2
        assert msg.data == 'voltage=1.3V'

    def test_find_all(self):
        # Exercise
        messages = self.service.find_all()
        # Verify
        addresses = {msg.address for msg in messages}
        assert 1123 in addresses
        assert 1124 in addresses
        assert 1125 in addresses

    def test_insert(self):
        # Exercise
        msg = Message(address=1127, priority=3, data='voltage=5.0V')
        created = self.service.insert(msg)
        # Verify
        assert created.address == 1127
        assert created.priority == 3
        assert created.data == 'voltage=5.0V'

    def test_update(self):
        # Exercise
        msg = Message(address=1123, priority=1, data='voltage=3.5V')
        updated = self.service.update(1123, msg)
        # Verify
        assert updated.address == 1123
        assert updated.priority == 1
        assert updated.data == 'voltage=3.5V'

    def test_delete(self):
        # Exercise
        self.service.delete(1125)
        # Verify
        addresses = {m.address for m in self.service.find_all()}
        assert 1125 not in addresses
