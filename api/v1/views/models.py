#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from models.brand import Brand
from models.model import Model
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from api.v1.views import *

parent_cls = Brand
child_cls = Model


@app_views.route(
    "/models",
    methods=["GET"],
    strict_slashes=False,
    defaults={"model_id": None},
)
@app_views.route("/models/<model_id>", methods=["GET"], strict_slashes=False)
def get_model(model_id):
    """Get all model or get a particular model by model id."""
    if model_id:
        return get_match(child_cls, model_id)
    model = [models.to_dict() for models in storage.all(Model).values()]
    return jsonify(model)


@app_views.route(
        "/brands/<brand_id>/models",
        methods=["GET"],
        strict_slashes=False,
)
def get_all_brand_model(brand_id):
    """Get all model or get a particular model by model id."""
    get_brand = storage.get(Brand, brand_id)
    if get_brand is None:
        abort(404)
    all_models = []
    for model in get_brand.models:
        all_models.append(model.to_dict())
    return jsonify(all_models)


@app_views.route(
    "/models/<model_id>",
    methods=["DELETE"],
    strict_slashes=False
)
def delete_model(model_id):
    """ Delete a brand by id."""
    return delete_match(child_cls, model_id)


@app_views.route(
    "/brands/<brand_id>/models",
    methods=["POST"],
    strict_slashes=False,
)
def create_model(brand_id):
    """Create a model via a POST request."""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    if "model_name" not in request.json:
        abort(400, description="Error: Missing name")
    if storage.get(parent_cls, brand_id) is None:
        abort(400, description="Error: Invalid Brand parameters")
    kwargs = request.get_json()
    return create_new(parent_cls, child_cls, brand_id, kwargs)


@app_views.route(
    "/models/<model_id>",
    methods=["PUT"],
    strict_slashes=False
)
def update_model(model_id):
    """Update a specfic model"""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    # validate if the current content exists
    get_model_obj = storage.get(child_cls, model_id)
    if not get_model_obj:
        abort(404, description="Object instance not found")
    kwargs = request.get_json()
    return update_match(get_model_obj, kwargs)
