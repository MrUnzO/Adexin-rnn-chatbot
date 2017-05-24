from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/", methods="")
def handle():
    return "ok"


if __name__ == '__main__':
    app.run()
