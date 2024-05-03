from models import User, db, Category, Todo

class UserService:
    
    def create(self, name, email, password):
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    def update(self, user_id, name, email):
        user = User.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
            return user
        return None
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return f"User with id {user_id} has been deleted."
        return None
    
    def get_by_id(self, user_id):
        return User.query.get(user_id)
    
    def get_all(self):
        return User.query.all()
    
    def get_by_email_and_password(self, email, password):
        return User.query.filter_by(email=email, password=password).first()
    

class TodoService:
    
    def create(self, user_id, title, description, due_date, category_ids=[]):
        todo = Todo(user_id=user_id, title=title, description=description, due_date=due_date)
        if category_ids:
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            todo.categories.extend(categories)
        db.session.add(todo)
        db.session.commit()
        return todo
    
    def update(self, todo_id, title=None, description=None, is_completed=False, due_date=None, category_ids=None):
        todo = Todo.query.get(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            todo.due_date = due_date
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
    
class CategoryService:
    
    def create(self, name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
    
    def update(self, category_id, name):
        category = Category.query.get(category_id)
        if category:
            category.name = name
            db.session.commit()
            return category
        return None
    
    def delete(self, category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return f"Category with id {category_id} has been deleted."
        return None
    
    def get_all(self):
        return Category.query.all()