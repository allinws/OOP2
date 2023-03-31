
from flask import Blueprint, render_template

bp = Blueprint('hello', __name__)

@bp.route('/')
def hello():
    return "Hello world"

@bp.route('/hello/', methods=["GET"])
@bp.route('/hello/<string:name>/', methods=["GET"])
def hello_template(name=None):
    return render_template('hello.html', name=name)