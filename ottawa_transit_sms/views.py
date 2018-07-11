from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return "Hi there! You're probably looking for something else."
