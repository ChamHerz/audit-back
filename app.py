from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
    'name': "Mi_tienda",
    'items': [{'name': "Mi_item", 'price': 15.99}]
}, {
    'name': "Mi_2da_tienda",
    'items': [{'name': "Mi_2item", 'price': 65.99}]
}]


@app.route('/')
def home():
    return 'ApiRest Start'


# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    # pass


# get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    # pass


# post /store data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)
    # pass


# put /store data: {name}
@app.route('/store/<string:name>', methods=['PUT'])
def update_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            store['name'] = request_data['name']
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    # pass


# delete /store/<name> data: {name}
@app.route('/store/<string:name>', methods=['DELETE'])
def delete_store(name):
    for store in stores:
        if store['name'] == name:
            index = stores.index(store)
            stores.pop(index)
            return jsonify({'message': 'ok'})
    return jsonify({'message': 'store not found'})
    # pass


if __name__ == '__main__':
    app.run()
