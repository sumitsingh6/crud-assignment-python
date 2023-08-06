from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import json
 
 
app = Flask(__name__)
 
app.secret_key = '555e051a9f814b689dfe94d9ac554e862bfb5c04'
 
app.config['MONGO_URI'] = "mongodb+srv://sumitkrsingh98:<password>@cluster0.0cfl7xx.mongodb.net/corider_users?retryWrites=true&w=majority"
 
mongo = PyMongo(app)
 
db = mongo.db.users
 
@app.route('/users', methods = ['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
 
    if _name and _email and _password and request.method == 'POST':
 
        _hashed_password = generate_password_hash(_password)
        insert_result = db.insert_one({
            'name': _name,
            'email': _email,
            'password': _hashed_password
        })
 
        # Access the inserted ID from the InsertOneResult object
        inserted_id = str(insert_result.inserted_id)
 
        # Convert the UpdateResult object to a Python dictionary
        response_data = {
            "acknowledged": insert_result.acknowledged,
            "inserted_id": inserted_id
        }

        return jsonify(response_data)
    else:
        return not_found()
 

#Get all users in databse
@app.route('/users')
def get_all_Users():
    userdata = db.find()
    resp = dumps(userdata)
    return jsonify(json.loads(resp))
 
 #Get a user by Id
@app.route('/users/<id>')
def get_user(id):
    user = db.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return jsonify(json.loads(resp))
 
 
@app.route('/users/<id>', methods = ['PUT'])
def update_user(id):
    _json = request.json
 
    if request.method == 'PUT':
 
        change_set = {}
 
        if 'name' in _json:
            change_set['name'] = _json['name']
 
        if 'email' in _json:
            change_set['email'] = _json['email']
 
        if 'password' in _json:
            _hashed_password = generate_password_hash(_json['password'])
            change_set['password'] = _hashed_password
 
        objId = ObjectId(id)
 
        update_result = db.update_one({'_id':objId}, {'$set': change_set})
        # Convert the UpdateResult object to a Python dictionary
        result_dict = {
            "acknowledged": update_result.acknowledged,
            "matched_count": update_result.matched_count,
            "modified_count": update_result.modified_count,
            "upserted_id": str(update_result.upserted_id) if update_result.upserted_id else None,
        }
        return jsonify(result_dict)
 
 
@app.route('/users/<id>', methods = ['DELETE'])
def delete_user(id):
    delete_result = db.delete_one({'_id': ObjectId(id)})
 
    # Construct a JSON response with the delete result information
    response_data = {
        "acknowledged": delete_result.acknowledged,
        "deleted_count": delete_result.deleted_count,
    }
 
    # Use Flask's jsonify function to return the JSON response
    return jsonify(response_data)
 
@app.errorhandler(404)
def not_found(error = True):
    message = {
        'status': 404,
        'message': 'Not Found '+request.url
    }
 
    resp = jsonify(message)
    resp.status_code = 404
    return resp
 
if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")