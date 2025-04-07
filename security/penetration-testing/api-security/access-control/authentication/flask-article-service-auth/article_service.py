from http import HTTPStatus
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

# Simulate a database table in a list
table = [
    {'id':1, 'description':'Effective Python','price':2390},
    {'id':2, 'description':'Effective Python','price':2390},
    {'id':3, 'description':'Effective Python','price':2390}
]

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "student": generate_password_hash("student"),
    "homer": generate_password_hash("duffbeer")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    else:
        return None


@app.route('/articles', methods = ['GET'])
@auth.login_required
def find_all():
    return jsonify({'data': table}), HTTPStatus.OK


@app.route('/articles/<int:oid>', methods = ['GET'])
@auth.login_required
def find_by_id(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'article not found'}), HTTPStatus.NOT_FOUND


@app.route('/articles', methods=['POST'])
@auth.login_required
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
@auth.login_required
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
@auth.login_required
def delete(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            table.remove(item)
            return '', HTTPStatus.NO_CONTENT
    return jsonify({'message': 'article not found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(port=8443, debug=True, ssl_context='adhoc')
