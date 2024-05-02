from flask import Blueprint, render_template, request

bp = Blueprint('hello', __name__)

@bp.route('/')
def hello():
    return render_template('welcome_form.html')

@bp.route('/login')
def login():
    return render_template('login_form.html')

@bp.route('/welcome', methods=["POST"])
def welcome():
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    return render_template('welcome.html', name=name, age=age, city=city)

@bp.route('/hello/', methods=["GET"])
@bp.route('/hello/<string:name>/', methods=["GET"])
def hello_template(name=None):
    return render_template('hello.html', name=name)