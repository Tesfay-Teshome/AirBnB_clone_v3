#!/usr/bin/python3
"""
the main app.py
"""


from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from werkzeug import exceptions

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(code):
    """call the close method of storage"""
    storage.close()

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0.")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
