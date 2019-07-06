from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.whiskey import whiskey_routes

    app.register_blueprint(whiskey_routes)
    return app
