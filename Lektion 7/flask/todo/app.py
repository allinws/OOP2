from flask import Flask
import models

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"


if __name__ == "__main__":
    models.Schema()
    app.run(debug=True)