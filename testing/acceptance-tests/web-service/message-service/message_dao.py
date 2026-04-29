import sqlite3
from message import Message


class MessageDao:
    """Data Access Object for the messages SQLite table."""

    def __init__(self, db_path: str = 'message.db') -> None:
        self.db_path = db_path

    # CRUD operations

    def find_all(self) -> list:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                'SELECT address, priority, data FROM messages'
            ).fetchall()
        return [Message(address=r[0], priority=r[1], data=r[2]) for r in rows]

    def find_by_id(self, address: int) -> Message | None:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                'SELECT address, priority, data FROM messages WHERE address = ?',
                (address,)
            ).fetchone()
        if row is None:
            return None
        return Message(address=row[0], priority=row[1], data=row[2])

    def insert(self, dto: Message) -> Message:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                'INSERT INTO messages (address, priority, data) VALUES (?, ?, ?)',
                (dto.address, dto.priority, dto.data)
            )
        return dto

    def update(self, address: int, dto: Message) -> Message | None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                'UPDATE messages SET priority = ?, data = ? WHERE address = ?',
                (dto.priority, dto.data, address)
            )
        if cursor.rowcount == 0:
            return None
        return Message(address=address, priority=dto.priority, data=dto.data)

    def delete(self, address: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                'DELETE FROM messages WHERE address = ?',
                (address,)
            )
        return cursor.rowcount > 0
