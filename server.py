import os
from flask import Flask

app = Flask(__name__)
endpoints = os.environ.get("ENDPOINTS", "/:hello").split(",")


def make_function(message):
    return lambda: message


for endpoint in endpoints:
    url, message = endpoint.split(":", 1)
    f = make_function(message)
    f.__name__ = url
    app.route(url)(f)


if __name__ == "__main__":
    app.run(threaded=True, port=os.environ.get("PORT", 8080), host="0.0.0.0")
