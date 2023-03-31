from flask import Blueprint, request, jsonify, render_template

from services.user_service import UserService

bp = Blueprint('users', __name__)

@bp.route('/users/', methods=["POST"])
def create_user():
    user_service = UserService()
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = user_service.create(name=name, email=email, password=password)
    user_dict = user.to_dict()
    return jsonify(user_dict), 201

@bp.route('/users/<int:user_id>/', methods=["PUT"])
def update_user(user_id):
    user_service = UserService()
    name = request.form.get('name')
    email = request.form.get('email')
    user = user_service.update(user_id=user_id, name=name, email=email)
    user_dict = user.to_dict()
    return jsonify(user_dict), 200

@bp.route('/users/<int:user_id>/', methods=["DELETE"])
def delete_user(user_id):
    user_service = UserService()
    user_service.delete(user_id=user_id)
    return 'User deleted', 204

@bp.route('/users/', methods=["GET"])
def get_all_users():
    user_service = UserService()
    users = user_service.get_all()
    user_dicts = [user.to_dict() for user in users]
    return jsonify(user_dicts), 200

@bp.route('/login/', methods=["POST"])
def login():
    user_service = UserService()
    email = request.form['email']
    password = request.form['password']
    user = user_service.get_by_email_and_password(email=email, password=password)
    if user:
        return render_template('logged_in.html', error=None, user=user)
    else:
        return render_template('logged_in.html', error="Invalid username/password"), 401
