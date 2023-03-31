from flask import Flask
from models.models import db, User, Todo
from routes import hello, users

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    db.init_app(app) # Initialisera appen in till SQLAlchemy
    with app.app_context():
        db.create_all() # Skapa alla tables (det vi gjorde med Schema förut)
    app.register_blueprint(users.bp)
    app.register_blueprint(hello.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
