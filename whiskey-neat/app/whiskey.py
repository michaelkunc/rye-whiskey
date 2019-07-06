from flask import Blueprint

whiskey_routes = Blueprint("whiskey", __name__, url_prefix="/whiskies")


@whiskey_routes.route("/")
def index():
    return "Here's where all the whiskey goes!"
