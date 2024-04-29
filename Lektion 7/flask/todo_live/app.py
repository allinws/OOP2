from flask import Flask, request, jsonify
import models
import services

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"


@app.route('/users/', methods=["POST"])
def create_user():
    user_service = services.UserService()
    body = request.get_json()
    name = body.get('name')
    email = body.get('email')
    user = user_service.create(name=name, email=email)
    return user, 201


if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)