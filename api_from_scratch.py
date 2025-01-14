
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Update with your MongoDB URI
mongo = PyMongo(app)

db = mongo.db  # Reference to the database

# Helper function to convert MongoDB documents to JSON
def user_to_json(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

# GET: Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    return jsonify([user_to_json(user) for user in users]), 200

# GET: Retrieve a single user by ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(user_to_json(user)), 200
    return jsonify({"error": "User not found"}), 404

# POST: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name and email are required"}), 400

    user_id = db.users.insert_one({"name": data['name'], "email": data['email']}).inserted_id
    new_user = db.users.find_one({"_id": user_id})
    return jsonify(user_to_json(new_user)), 201

# PUT: Update a user by ID
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    update_data = {}

    if "name" in data:
        update_data["name"] = data["name"]
    if "email" in data:
        update_data["email"] = data["email"]

    result = db.users.update_one({"_id": ObjectId(id)}, {"$set": update_data})

    if result.matched_count > 0:
        updated_user = db.users.find_one({"_id": ObjectId(id)})
        return jsonify(user_to_json(updated_user)), 200
    return jsonify({"error": "User not found"}), 404

# DELETE: Delete a user by ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = db.users.delete_one({"_id": ObjectId(id)})

    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
