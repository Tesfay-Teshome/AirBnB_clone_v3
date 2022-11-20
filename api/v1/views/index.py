#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

stat_dict = {
    "amenities": "Amenities",
    "cities": "Cities",
    "places": "Places",
    "reviews": "Reviews",
    "states": "States",
    "users": "Users"
}

@app_views.route('/status', strict_slashes=False)
def status():
    """return the status of the api"""
    status = {"status": "OK"}
    return jsonify(status)

@app_views.route('/stats', strict_slashes=False)
def stats():
    """create an endpoint that retrieves the
    number of each objects by type
    """
    stat = {}
    for key, Value in stat_dict.items():
        stat[key] = storage.count(Value)
    return jsonify(stat)

