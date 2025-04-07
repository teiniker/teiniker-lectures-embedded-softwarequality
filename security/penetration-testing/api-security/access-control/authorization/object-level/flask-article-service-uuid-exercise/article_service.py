from http import HTTPStatus
from flask import Flask, jsonify, request

# Simulate a database table in a list
table = [
    {'id':1, 'description':'Effective Python','price':2390}
]

app = Flask(__name__)

@app.route('/articles', methods = ['GET'])
def find_all():
    return jsonify({'data': table}), HTTPStatus.OK


@app.route('/articles/<int:oid>', methods = ['GET'])
def find_by_id(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'article not found'}), HTTPStatus.NOT_FOUND


@app.route('/articles', methods=['POST'])
def insert():
    data = request.get_json()
    print(data)
    oid = data.get('id')
    description = data.get('description')
    price = data.get('price')
    article = {
        'id': oid,
        'description': description,
        'price': price
    }
    table.append(article)
    return jsonify(article), HTTPStatus.CREATED


@app.route('/articles/<int:oid>', methods=['PUT'])
def update(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            data = request.get_json()
            print(data)
            item.update({'description':data.get('description'), 'price':data.get('price')})
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'article not found'}), HTTPStatus.NOT_FOUND


@app.route('/articles/<int:oid>', methods=['DELETE'])
def delete(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            table.remove(item)
            return '', HTTPStatus.NO_CONTENT
    return jsonify({'message': 'article not found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(port=8080, debug=True)
