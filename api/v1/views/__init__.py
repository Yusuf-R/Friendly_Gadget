#!/usr/bin/env python3
"""model for blue print view"""
from flask import Blueprint, make_response, jsonify, abort
from models import storage
from models.brand import Brand
from models.model import Model
from models.feature import Feature
from models.secondary_feature import Secondary

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


def get_match(cls, id):
    """GET: get the object of a specific class based on its id"""
    obj = storage.get(cls, id)
    if obj:
        return jsonify(obj.to_dict())
    abort(404)


def delete_match(cls, id):
    """DELETE: delete the object of a specific class based on its id"""
    obj = storage.get(cls, id)
    if obj:
        storage.delete(obj)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


def create_new(p_cls, ch_cls, p_id, kwargs):
    """POST: creating a new object for the class"""
    if p_cls == Brand and ch_cls is None:
        obj = p_cls(**kwargs)
        obj.save()
        return jsonify(obj.to_dict()), 201
    if p_cls == Brand and ch_cls == Model:
        kwargs["brand_id"] = p_id
        obj = ch_cls(**kwargs)
        obj.save()
        return jsonify(obj.to_dict()), 201
    if p_cls == Model and ch_cls == Feature:
        kwargs["model_id"] = p_id
        obj = ch_cls(**kwargs)
        obj.save()
        for _, val in kwargs.items():
            if isinstance(val, dict):
                for s_k, s_v in val.items():
                    s_cls = Secondary(feature_id=obj.id)
                    s_cls.inner_key = s_k
                    s_cls.inner_value = s_v
                    s_cls.save()
        return jsonify(obj.to_dict()), 201
    else:
        abort(404)


def update_match(obj, kwargs):
    """PUT: update the brand object"""
    exempt = [
            "id",
            "brand_id",
            "model_id",
            "feature_id",
            "secondary_id",
            ]
    for key, value in kwargs.items():
        if key not in exempt:
            setattr(obj, key, value)
    obj.save()
    ret_data = jsonify(obj.to_dict())
    if obj.secondary_details:
        for _, val in kwargs.items():
            if isinstance(val, dict):
                for s_k, s_v in val.items():
                    for i in obj.secondary_details:
                        if i.inner_key == s_k and i.feature_id == obj.id:
                            i.inner_key = s_k
                            i.inner_value = s_v
                            i.save()
                        else:
                            continue
    return make_response(ret_data, 200)


# used to instantiate the blueprint routes upon program start-up
from api.v1.views.status import *
from api.v1.views.brands import *
from api.v1.views.models import *
from api.v1.views.features import *
from api.v1.views.secondary_features import *
