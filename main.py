from flask import Flask, request

from src.classes.create_class import create_class
from src.classes.delete_class import delete_class
from src.classes.join_class import join_class
from src.classes.leave_class import leave_class
from src.group.create_group import create_group
from src.group.join_group import join_group

app = Flask(__name__)


@app.route('/')
def root():
    request_json = request.get_json()
    if request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'World'
    return 'Hello, {}!'.format(name)


@app.route('/class', methods=['POST'])
def class_post():
    args = request.args
    user_id = args.get('userID')
    name = args.get('name')

    create_class(user_id, name)
    return 'OK'


@app.route('/class', methods=['DELETE'])
def class_remove():
    args = request.args
    user_id = args.get('userID')
    class_id = args.get('classID')

    delete_class(class_id, user_id)
    return 'OK'


@app.route('/class/<class_code>', methods=['POST'])
def class_id_post(class_code):
    args = request.args
    user_id = args.get('userID')

    join_class(user_id, class_code)
    return 'OK'


@app.route('/class/<class_id>', methods=['DELETE'])
def class_id_delete(class_id):
    args = request.args
    user_id = args.get('userID')

    leave_class(user_id, class_id)
    return 'OK'


@app.route('/class/<class_id>/groups', methods=['POST'])
def groups_post(class_id):
    body = request.get_json()

    create_group(class_id, body['date'], body['location'], body['description'])
    return 'OK'


@app.route('/class/<class_id>/groups/<group_id>', methods=['POST'])
def group_id_post(class_id, group_id):
    args = request.args
    user_id = args.get('user_id')
    ride = args.get('ride')

    join_group(class_id, group_id, user_id, ride)
    return 'OK'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
