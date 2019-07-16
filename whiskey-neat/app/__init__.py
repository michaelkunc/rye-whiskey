from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.whiskey import whiskey_routes

    app.register_blueprint(whiskey_routes)

    @app.route("/")
    def home():
        return "Welcome to the home of delicious whiskey"

    return app
