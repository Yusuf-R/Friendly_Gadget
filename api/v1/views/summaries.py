#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from models.model import Model
from models.summary import Summary
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from api.v1.views import create_new, get_match, delete_match, update_match

parent_cls = Model
child_cls = Summary


@app_views.route(
    "/summaries",
    methods=["GET"],
    strict_slashes=False,
    defaults={"summary_id": None},
)
@app_views.route(
        "/summaries/<summary_id>",
        methods=["GET"],
        strict_slashes=False
)
def get_summary(summary_id):
    """Get all summary of all model or get a particular model by summary id."""
    if summary_id:
        return get_match(child_cls, summary_id)
    summary = [model.to_dict() for model in storage.all(Summary).values()]
    return jsonify(summary)


@app_views.route(
    "/models/<model_id>/summaries",
    methods=["GET"],
    strict_slashes=False,
)
def get_all_model_summary(model_id):
    """Get all summary of all model base on the brand id"""
    get_model = storage.get(Model, model_id)
    if get_model is None:
        abort(404)
    all_models = []
    for model in get_model.summaries:
        all_models.append(model.to_dict())
    return jsonify(all_models)


@app_views.route(
    "/summaries/<summary_id>",
    methods=["DELETE"],
    strict_slashes=False
)
def delete_summary(summary_id):
    """Delete a brand by id."""
    return delete_match(child_cls, summary_id)


@app_views.route(
    "/models/<model_id>/summaries",
    methods=["POST"],
    strict_slashes=False,
)
def create_summary(model_id):
    """Create a summary via a POST request."""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    if storage.get(Model, model_id) is None:
        abort(404, description="Object instance not found")
    kwargs = request.get_json()
    return create_new(parent_cls, child_cls, model_id, kwargs)


@app_views.route(
    "/summaries/<summary_id>",
    methods=["PUT"],
    strict_slashes=False
)
def update_summary_model(summary_id):
    """Update a brand by id."""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    # validate if the current content exists
    get_summary_obj = storage.get(child_cls, summary_id)
    if not get_summary_obj:
        abort(404, description="Object instance not found")
    kwargs = request.get_json()
    return update_match(get_summary_obj, kwargs)
