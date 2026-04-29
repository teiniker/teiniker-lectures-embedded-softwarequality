import requests
from message import Message


class ServiceError(Exception):
    pass


class MessageService:

    def __init__(self, base_url='http://localhost:8080/messages'):
        self.base_url = base_url

    def find_all(self) -> list:
        response = requests.get(self.base_url, timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_all() failed: {response.status_code}')
        return [self._to_message(m) for m in response.json()['data']]

    def find_by_id(self, address: int) -> Message:
        response = requests.get(f'{self.base_url}/{address}', timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_by_id({address}) failed: {response.status_code}')
        return self._to_message(response.json())

    def insert(self, message: Message) -> Message:
        response = requests.post(self.base_url, timeout=5, json=self._to_dict(message))
        if response.status_code != 201:
            raise ServiceError(f'insert() failed: {response.status_code}')
        return self._to_message(response.json())

    def update(self, address: int, message: Message) -> Message:
        response = requests.put(f'{self.base_url}/{address}', timeout=5,
                                json=self._to_dict(message))
        if response.status_code != 200:
            raise ServiceError(f'update({address}) failed: {response.status_code}')
        return self._to_message(response.json())

    def delete(self, address: int) -> None:
        response = requests.delete(f'{self.base_url}/{address}', timeout=5)
        if response.status_code != 204:
            raise ServiceError(f'delete({address}) failed: {response.status_code}')

    def _to_message(self, data: dict) -> Message:
        return Message(
            address=data['address'],
            priority=data['priority'],
            data=data['data']
        )

    def _to_dict(self, message: Message) -> dict:
        return {
            'address': message.address,
            'priority': message.priority,
            'data': message.data
        }
