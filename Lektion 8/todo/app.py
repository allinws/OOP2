from flask import Flask
from .models import models
from .routes import hello, users


def create_app():
    app = Flask(__name__)
    app.register_blueprint(users.bp)
    app.register_blueprint(hello.bp)
    models.Schema()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)