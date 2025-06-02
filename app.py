from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['user_db']
collection = db['users']

@app.route('/')
def home():
    
    return "API is working"

# ? Create User
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"message": "User added", "id": str(result.inserted_id)})

# ???? Read all users
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in collection.find():
        user['_id'] = str(user['_id'])  # ObjectId to string
        users.append(user)
    return jsonify(users)

# ???? Read single user
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# ?? Update user
@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    result = collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": data}
    )
    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"message": "No changes made or user not found"})

# ? Delete user
@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"message": "User not found"})

if __name__ == '__main__':
    app.run(debug=True)
