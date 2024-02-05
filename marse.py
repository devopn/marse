from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "<b>Миссия Колонизация Марса</b>"

@app.route("/<titles>")
# @app.route("/index/<title>")
def index(titles):
    return render_template("base.html", title=titles)


@app.route("/index")
def index():
    return "<b>И на Марсе будут яблони цвести!</b>"


@app.route("/promotion")
def promotion():
    strings = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    ]
    return "<br>".join(strings)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img height=500 src="https://upload.wikimedia.org/wikipedia/commons/0/0c/Mars_-_August_30_2021_-_Flickr_-_Kevin_M._Gill.png">
                    <div>Вот она какая, красная планета.</div>
                  </body>
                </html>"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
