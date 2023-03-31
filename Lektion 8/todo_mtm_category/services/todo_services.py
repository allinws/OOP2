from models.models import Todo, Category, db

class TodoService:
    
    def create(self, user_id, title, description, due_date, category_ids=None):
        todo = Todo(user_id=user_id, title=title, description=description, due_date=due_date)
        if category_ids:
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            todo.categories.extend(categories)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    def update(self, todo_id, title=None, description=None, is_completed=None, due_date=None, category_ids=None):
        todo = Todo.query.get(todo_id)
        if todo:
            if title:
                todo.title = title
            if description:
                todo.description = description
            if due_date:
                todo.due_date = due_date
            if is_completed is not None:
                todo.is_completed = is_completed
            if category_ids:
                categories = Category.query.filter(Category.id.in_(category_ids)).all()
                todo.categories = categories
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
