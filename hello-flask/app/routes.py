from app import app


@app.route("/")
@app.route("/index")
def app():
    return "What up Cameo??"

