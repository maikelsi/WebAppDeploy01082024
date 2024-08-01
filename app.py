from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi

import os

TITULO = os.getenv("TITULO")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("SEU_HTML.html", titulo=TITULO)


asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run()