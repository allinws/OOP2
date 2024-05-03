import datetime
from flask import Flask, request, jsonify, render_template
from models import db, User
from services import UserService, CategoryService, TodoService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alexdb.sqlite'

db.init_app(app)

with app.app_context():
    db.create_all()  # Create all tables

""" USERS """

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

@app.route('/users/<int:user_id>/', methods=["PATCH"])
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
        return render_template('logged_in.html', error="Invalid username/password", user=None), 401


""" TODOS """

@app.route('/todos/', methods=["POST"])
def create_todo():
    todo_service = TodoService()
    data = request.get_json()
    title = data['title']
    description = data['description']
    due_date = data.get('due_date')
    user_id = data.get('user_id')
    category_ids = data.get('category_ids', [])
    if due_date:
        due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    todo = todo_service.create(title=title, description=description, due_date=due_date, user_id=user_id, category_ids=category_ids)
    todo_dict = todo.to_dict()
    return jsonify(todo_dict), 201

@app.route('/todos/<int:todo_id>/', methods=["PUT"])
def update_todo(todo_id):
    todo_service = TodoService()
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    is_completed = data.get('is_completed', False)  # Defaults to False if not provided
    due_date = data.get('due_date')
    if due_date:
        due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    todo = todo_service.update(todo_id=todo_id, title=title, description=description, is_completed=is_completed, due_date=due_date)
    todo_dict = todo.to_dict()
    return jsonify(todo_dict), 200

@app.route('/todos/<int:todo_id>/', methods=["DELETE"])
def delete_todo(todo_id):
    todo_service = TodoService()
    todo_service.delete(todo_id=todo_id)
    return 'Todo deleted', 204

@app.route('/todos/', methods=["GET"])
def get_all_todos():
    todo_service = TodoService()
    todos = todo_service.get_all()
    todo_dicts = [todo.to_dict() for todo in todos]
    return jsonify(todo_dicts), 200

@app.route('/todos/completed/', methods=["GET"])
def get_completed_todos():
    todo_service = TodoService()
    todos = todo_service.get_completed()
    todo_dicts = [todo.to_dict() for todo in todos]
    return jsonify(todo_dicts), 200


""" CATEGORIES """

@app.route('/categories/', methods=["GET"])
def get_all_categories():
    category_service = CategoryService()
    categories = category_service.get_all()
    category_dicts = [category.to_dict() for category in categories]
    return jsonify(category_dicts), 200

@app.route('/categories/', methods=["POST"])
def create_category():
    category_service = CategoryService()
    data = request.get_json()
    name = data['name']
    category = category_service.create(name=name)
    category_dict = category.to_dict()
    return jsonify(category_dict), 201

@app.route('/categories/<int:category_id>/', methods=["PUT"])
def update_category(category_id):
    category_service = CategoryService()
    data = request.get_json()
    name = data.get('name')
    category = category_service.update(category_id=category_id, name=name)
    if category:
        category_dict = category.to_dict()
        return jsonify(category_dict), 200
    else:
        return 'Category not found', 404

@app.route('/categories/<int:category_id>/', methods=["DELETE"])
def delete_category(category_id):
    category_service = CategoryService()
    result = category_service.delete(category_id=category_id)
    if result:
        return 'Category deleted', 204
    else:
        return 'Category not found', 404


if __name__ == "__main__":
    app.run(debug=True)
