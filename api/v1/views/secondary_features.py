#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from api.v1.views import get_match
from models.secondary_feature import Secondary

child_cls = Secondary


@app_views.route(
    "/secondary",
    methods=["GET"],
    strict_slashes=False,
    defaults={"sec_id": None},
)
@app_views.route(
    "/secondary/<sec_id>", methods=["GET"], strict_slashes=False
)
def get_secondary(sec_id):
    """Get all sec_feature or a specific sec_feature by sec_id."""
    if sec_id:
        return get_match(child_cls, sec_id)
    sec_feature = [
        sec_feat.to_dict() for sec_feat in storage.all(Secondary).values()
    ]
    return jsonify(sec_feature)
