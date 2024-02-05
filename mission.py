from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<titles>")
# @app.route("/index/<title>")
def index(titles):
    return render_template("base.html", title=titles)

app.run("127.0.0.1", 8080)