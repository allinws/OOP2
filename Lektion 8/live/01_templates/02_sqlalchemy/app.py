from flask import Flask, request, jsonify, render_template
from models import db, User
from services import UserService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'

db.init_app(app)

with app.app_context():
    db.create_all()  # Create all tables

@app.route('/users/', methods=["POST"])
def create_user():
    user_service = UserService()
    body = request.get_json()
    name = body['name']
    email = body['email']
    password = body['password']
    user = user_service.create(name=name, email=email, password=password)
    user_dict = user.to_dict()
    return jsonify(user_dict), 201

@app.route('/users/<int:user_id>/', methods=["PUT"])
def update_user(user_id):
    user_service = UserService()
    body = request.get_json()
    name = body['name']
    email = body['email']
    user = user_service.update(user_id=user_id, name=name, email=email)
    user_dict = user.to_dict()
    return jsonify(user_dict), 200

@app.route('/users/<int:user_id>/', methods=["DELETE"])
def delete_user(user_id):
    user_service = UserService()
    user_service.delete(user_id=user_id)
    return 'User deleted', 204

@app.route('/users/', methods=["GET"])
def get_all_users():
    user_service = UserService()
    users = user_service.get_all()
    user_dicts = [user.to_dict() for user in users]
    return jsonify(user_dicts), 200

@app.route('/login/', methods=["POST"])
def login():
    user_service = UserService()
    body = request.get_json()
    email = body['email']
    password = body['password']
    user = user_service.get_by_email_and_password(email=email, password=password)
    if user:
        return render_template('logged_in.html', error=None, user=user)
    else:
        return render_template('logged_in.html', error="Invalid username/password"), 401

if __name__ == "__main__":
    app.run(debug=True)
