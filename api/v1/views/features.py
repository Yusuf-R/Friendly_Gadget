#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from models.model import Model
from models.feature import Feature
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from api.v1.views import update_match, delete_match, create_new, get_match

parent_cls = Model
child_cls = Feature


@app_views.route(
    "/features",
    methods=["GET"],
    strict_slashes=False,
    defaults={"feature_id": None},
)
@app_views.route(
    "/features/<feature_id>", methods=["GET"], strict_slashes=False
)
def get_feature(feature_id):
    """Get all feature or get a particular feature by feature id."""
    if feature_id:
        return get_match(child_cls, feature_id)
    feature = [
        features.to_dict() for features in storage.all(Feature).values()
    ]
    return jsonify(feature)


@app_views.route(
    "/models/<model_id>/features",
    methods=["GET"],
    strict_slashes=False,
)
def get_all_model_feature(model_id):
    """Get all feature for a particular model by model id."""
    get_model = storage.get(Model, model_id)
    if get_model is None:
        abort(404)
    all_features = []
    for features in get_model.features:
        all_features.append(features.to_dict())
    return jsonify(all_features)


@app_views.route(
    "/features/<feature_id>", methods=["DELETE"], strict_slashes=False
)
def delete_feature(feature_id):
    """Delete a brand by id."""
    return delete_match(child_cls, feature_id)


@app_views.route(
    "/models/<model_id>/features",
    methods=["POST"],
    strict_slashes=False,
)
def create_feature(model_id):
    """Create a model via a POST request"""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    if storage.get(parent_cls, model_id) is None:
        abort(400, description="Error: Invalid Model parameters")
    kwargs = request.get_json()
    return create_new(parent_cls, child_cls, model_id, kwargs)


@app_views.route(
    "/features/<feature_id>", methods=["PUT"], strict_slashes=False
)
def update_feature(feature_id):
    """Update a specfic feature"""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    # validate if the current content exists
    get_feature_obj = storage.get(child_cls, feature_id)
    if not get_feature_obj:
        abort(404, description="Object instance not found")
    kwargs = request.get_json()
    return update_match(get_feature_obj, kwargs)
