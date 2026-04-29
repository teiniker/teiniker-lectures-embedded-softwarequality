from http import HTTPStatus
from flask import Flask, jsonify, request

# Simulate a database table in a list
table = [
    {'address': 1123, 'priority': 2, 'data':'voltage=3.4V'},
    {'address': 1124, 'priority': 2, 'data':'voltage=1.3V'},
    {'address': 1125, 'priority': 1, 'data':'voltage=-1.7V'}
]

app = Flask(__name__)

@app.route('/messages', methods = ['GET'])
def find_all():
    return jsonify({'data': table}), HTTPStatus.OK


@app.route('/messages/<int:address>', methods = ['GET'])
def find_by_id(address):
    for item in table:
        print(item)
        if item['address'] == address:
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND


@app.route('/messages', methods=['POST'])
def insert():
    data = request.get_json()
    print(data)
    address = data.get('address')
    priority = data.get('priority')
    message_data = data.get('data')
    message = {
        'address': address,
        'priority': priority,
        'data': message_data
    }
    table.append(message)
    return jsonify(message), HTTPStatus.CREATED


@app.route('/messages/<int:address>', methods=['PUT'])
def update(address):
    for item in table:
        print(item)
        if item['address'] == address:
            data = request.get_json()
            print(data)
            item.update({'priority':data.get('priority'), 'data':data.get('data')})
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND


@app.route('/messages/<int:address>', methods=['DELETE'])
def delete(address):
    for item in table:
        print(item)
        if item['address'] == address:
            table.remove(item)
            return '', HTTPStatus.NO_CONTENT
    return jsonify({'message': 'message not found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(port=8080, debug=True)
