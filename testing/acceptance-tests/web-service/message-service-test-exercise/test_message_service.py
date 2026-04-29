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
    # TODO: Implement the test cases for the MessageService methods
    pass
