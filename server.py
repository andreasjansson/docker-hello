import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return os.environ.get("MESSAGE", "hello world")


if __name__ == "__main__":
    app.run(threaded=True, port=os.environ.get("PORT", 8080), host="0.0.0.0")
