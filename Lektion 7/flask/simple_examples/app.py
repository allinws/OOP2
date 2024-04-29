from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def hello():
#     print('hello')
#     return "Hello world"

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def handle_request():
    if request.method == 'POST':
        body = request.get_json()
        print('body', body)
        return 'Success!'
    elif request.method == 'GET':
        return 'Hello, world!'
    elif request.method == 'DELETE':
        return 'Deleted!'
    elif request.method == 'PUT':
        return 'Updated!'
    

if __name__ == "__main__":
    app.run(debug=True)
