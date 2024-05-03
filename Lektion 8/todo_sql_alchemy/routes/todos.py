from flask import Blueprint, request, jsonify
from datetime import datetime
from ..services.todo_services import TodoService

bp = Blueprint('todos', __name__)

@bp.route('/todos/', methods=["POST"])
def create_todo():
    todo_service = TodoService()
    title = request.form['title']
    description = request.form['description']
    due_date = request.form.get('due_date')
    user_id = request.form.get('user_id')
    if due_date:
        due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    todo = todo_service.create(title=title, description=description, due_date=due_date, user_id=user_id)
    todo_dict = todo.to_dict()
    return jsonify(todo_dict), 201

@bp.route('/todos/<int:todo_id>/', methods=["PUT"])
def update_todo(todo_id):
    todo_service = TodoService()
    title = request.form.get('title')
    description = request.form.get('description')
    is_completed = request.form.get('is_completed').lower() == 'true'
    due_date = request.form.get('due_date')
    if due_date:
        due_date = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    todo = todo_service.update(todo_id=todo_id, title=title, description=description, is_completed=is_completed, due_date=due_date)
    todo_dict = todo.to_dict()
    return jsonify(todo_dict), 200

@bp.route('/todos/<int:todo_id>/', methods=["DELETE"])
def delete_todo(todo_id):
    todo_service = TodoService()
    todo_service.delete(todo_id=todo_id)
    return 'Todo deleted', 204

@bp.route('/todos/', methods=["GET"])
def get_all_todos():
    todo_service = TodoService()
    todos = todo_service.get_all()
    # todo_dicts = [todo.to_dict() for todo in todos]
    todo_dicts = []
    for todo in todos:
        todo_dicts.append(todo.to_dict())
    return jsonify(todo_dicts), 200

@bp.route('/todos/completed/', methods=["GET"])
def get_completed_todos():
    todo_service = TodoService()
    todos = todo_service.get_completed()
    todo_dicts = [todo.to_dict() for todo in todos]
    return jsonify(todo_dicts), 200

