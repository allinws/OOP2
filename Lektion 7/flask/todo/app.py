from flask import Flask, request, jsonify
import models
import service

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route('/users/', methods=["POST"])
def create_user():
    user_service = service.UserService()
    name = request.form.get('name')
    email = request.form.get('email')
    user = user_service.create(name=name, email=email)
    return user, 201

@app.route('/users/<int:user_id>/', methods=["PUT"])
def update_user(user_id):
    user_service = service.UserService()
    name = request.form.get('name')
    email = request.form.get('email')
    user = user_service.update(user_id=user_id, name=name, email=email)
    return user, 200

@app.route('/users/<int:user_id>/', methods=["DELETE"])
def delete_user(user_id):
    user_service = service.UserService()
    user = user_service.delete(user_id=user_id)
    return user, 204

if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)