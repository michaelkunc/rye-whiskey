from flask import Blueprint
from app.models import Whiskey

whiskey_routes = Blueprint("whiskey", __name__, url_prefix="/whiskies")


@whiskey_routes.route("/")
def index():
    return str(Whiskey())
