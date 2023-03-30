# Importerar Flask
from flask import Flask

# Skapar en ny Flask-app
app = Flask(__name__)


# Skapar en ny route som skriver ut "Hello world"
@app.route('/')
def hello():
    return "Hello world"

# Skapar en ny route som tar emot ett namn
@app.route("/<name>/")
def hello_name(name):
    return f"Hello {name}"

# Startar servern när vi kör python-filen
if __name__ == "__main__":
    app.run(debug=True)