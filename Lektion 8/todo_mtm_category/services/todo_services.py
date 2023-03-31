from models.models import Todo, db

class TodoService:
    
    def create(self, user_id, title, description, due_date):
        todo = Todo(user_id=user_id, title=title, description=description, due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    def update(self, todo_id, title, description, is_completed, due_date):
        todo = Todo.query.get(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            todo.due_date = due_date
            todo.is_completed = is_completed
            db.session.commit()
            return todo
        return None
    
    def delete(self, todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return f"Todo with id {todo_id} has been deleted."
        return None
    
    
    def get_all_by_user(self, user_id):
        return Todo.query.filter_by(user_id=user_id).all()
    
    def get_completed(self):
        return Todo.query.filter_by(is_completed=True).all()
    
    def get_all(self):
        return Todo.query.all()