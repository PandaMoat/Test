#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
app = Flask(__name__)

users= [
      {
          'id': 1,
          'username' : u'Ben',
          'email' : u'Ben@Localhost.com',
          'done':False},
      {
          'id': 2,
          'username': u'Frank', 
          'email': u'Frank@email.com',
          'done': False}
]

@app.route('/todo/api/v1.0/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
       abort(404)
    return jsonify(user[0]['username'],user[0]['email'])
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify('Bush did 9/11'), 404)

@app.route('/todo/api/v1.0/users', methods=['POST'])
def create_user():
     if not request.json or not 'username' in request.json:
         abort(400)
     user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
        'email': request.json.get('email', " "),
        'done': False}
     users.append(user)
     return jsonify({'user': user}), 201
    
@app.route('/todo/api/v1.0/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user= [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'username' in request.json and type(request.json['username']) != unicode:
        abort(400)
    if 'email' in request.json and type(request.json['email']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    user[0]['username'] = request.json.get('username', user[0]['username'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['done'] = request.json.get('done', user[0]['done'])
    return jsonify({'user': user[0]})
@app.route('/todo/api/v1.0/users/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})
if __name__ == '__main__':
    app.run(debug=True)



