from flask import Flask
import models
import service

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

@app.route('/users/', methods=["POST"])
def create_user():
    user_service = service.UserService()
    user_service.create(name='John', email='john@gmail.com')
    return "User created", 201

if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)