"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import Family
from random import randint
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = Family("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members')
def handle_members():

    if request.method == 'GET':
        # this is how you can use the Family datastructure by calling its methods
        members = jackson_family.get_all_members()

        return jsonify(members), 200

@app.route('/member', methods=['POST'])
def handle_create_member():

    if request.method == 'POST':

        data = request.get_json()

        if not data:
            return jsonify({"message":"Invalid request data"}), 400
        
        new_member = {
            "id": data.get("id"),
            "first_name": data.get("first_name", "unknown"),
            "last_name": data.get("last_name", "Jackson"),
            "age": data.get("age"),
            "lucky_number": data.get("lucky_number")
        }

        if "id" not in data:
            new_member["id"] = jackson_family._generateId()

        jackson_family.add_member(new_member)
        return jsonify({"message": "Member added successfully"}), 200

@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def handle_member(member_id):

    if request.method == 'GET':
        member = jackson_family.get_member(member_id)
        print("printing member")
        print(member)
        return jsonify(member), 200
    
    elif request.method == 'DELETE':
        member = jackson_family.delete_member(member_id)
        return jsonify({"done":True}), 200
        



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
