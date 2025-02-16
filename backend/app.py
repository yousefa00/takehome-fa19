from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/contacts", methods=['GET'])
def get_contacts():
    hobby = request.args.get('hobby')  # Retrieves hobby query param
    if hobby is not None:  # Checks if a hobby param existed
        if db.getByHobby('contacts', hobby) is None:
            return create_response(status=404, message="No contact with this hobby exists")
        return create_response({"contacts": db.getByHobby('contacts', hobby)})
    return create_response({"contacts": db.get('contacts')})  # If no hobby param existed, this runs

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")
    db.deleteById('contacts', int(id))
    return create_response(message="Contact deleted")

@app.route("/contacts/<id>", methods=['GET'])
def get_contact_with_id(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")
    return create_response({"contacts": db.getById('contacts', int(id))})

@app.route("/contacts", methods=['POST'])
def add_contact():
    data = request.json
    missing_field = []

    if not check_if_key_exists(data, "name"):
        missing_field.append("name")
    if not check_if_key_exists(data, "nickname"):
        missing_field.append("nickname")
    if not check_if_key_exists(data, "hobby"):
        missing_field.append("hobby")

    if len(missing_field) > 0:
        return create_response(status=422, message="Missing field(s): " + ", ".join(missing_field))
    return create_response(status=201, data={"contacts": db.create('contacts', data)})

@app.route("/contacts/<id>", methods=['PUT'])
def update_contact(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")

    data = request.json
    if check_if_key_exists(data, "name") or check_if_key_exists(data, "hobby"):
        return create_response(status=201, data={"contacts": db.updateById('contacts', int(id), data)})
    return create_response({"contacts": db.getById('contacts', int(id))})

def check_if_key_exists(dictionary, key):
    return key in dictionary

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
