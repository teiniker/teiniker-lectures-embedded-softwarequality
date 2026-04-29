from http import HTTPStatus
from flask import Flask, jsonify, request
from message import Message
from message_dao import MessageDao

app = Flask(__name__)
dao = MessageDao()


@app.route('/messages', methods=['GET'])
def find_all():
    messages = dao.find_all()
    return jsonify({'data': [_to_dict(m) for m in messages]}), HTTPStatus.OK


@app.route('/messages/<int:address>', methods=['GET'])
def find_by_id(address):
    msg = dao.find_by_id(address)
    if msg is None:
        return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND
    return jsonify(_to_dict(msg)), HTTPStatus.OK


@app.route('/messages', methods=['POST'])
def insert():
    data = request.get_json()
    dto = Message(
        address=data.get('address'),
        priority=data.get('priority'),
        data=data.get('data')
    )
    created = dao.insert(dto)
    return jsonify(_to_dict(created)), HTTPStatus.CREATED


@app.route('/messages/<int:address>', methods=['PUT'])
def update(address):
    data = request.get_json()
    dto = Message(
        address=address,
        priority=data.get('priority'),
        data=data.get('data')
    )
    updated = dao.update(address, dto)
    if updated is None:
        return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND
    return jsonify(_to_dict(updated)), HTTPStatus.OK


@app.route('/messages/<int:address>', methods=['DELETE'])
def delete(address):
    found = dao.delete(address)
    if not found:
        return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND
    return '', HTTPStatus.NO_CONTENT


def _to_dict(dto: Message) -> dict:
    return {'address': dto.address, 'priority': dto.priority, 'data': dto.data}


if __name__ == '__main__':
    app.run(port=8080, debug=True)
