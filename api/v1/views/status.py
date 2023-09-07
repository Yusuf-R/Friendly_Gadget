#!/usr/bin/env python3
"""module for index route"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.brand import Brand
from models.model import Model
from models.feature import Feature
from models.secondary_feature import Secondary


@app_views.route("/status", methods=["GET"])
def status():
    """index route"""
    status = {"status": "OK"}
    return jsonify(status), 200


@app_views.route("/statistics", methods=["GET"])
def stats():
    """statisitcs of the database count"""
    return (
        jsonify(
            {
                "brands": storage.count(Brand),
                "models": storage.count(Model),
                "features": storage.count(Feature),
                "secondary": storage.count(Secondary),
            }
        ),
        200,
    )
