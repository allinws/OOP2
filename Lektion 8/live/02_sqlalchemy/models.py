from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoCategory(db.Model):
    __tablename__ = 'todo_category'
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)

    def __repr__(self):
        return f"<TodoCategory todo_id={self.todo_id}, category_id={self.category_id}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False) #unique=True,
    password = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<User {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        }

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    due_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    categories = db.relationship('Category', secondary='todo_category', backref='todos', lazy='dynamic')

    def __repr__(self):
        return f'<Todo {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_completed': self.is_completed,
            'created_on': self.created_on.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'user_id': self.user_id,
            'categories': [category.to_dict() for category in self.categories]
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    # todos = db.relationship('Todo', secondary='todo_category', backref='todo_categories', lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
