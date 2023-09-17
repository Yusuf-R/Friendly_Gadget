#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from ast import mod

from sqlalchemy.sql.functions import mode
from models import brand
from models.brand import Brand
from models.model import Model
from flask import Flask, render_template, request, jsonify
from models import storage
from models.summary import Summary

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
# @app.route('/friendly_gadget', strict_slashes=False)
def index():
    """The homepage of the application."""
    brand_name = []
    # get all brands_name
    brands = storage.all(Brand).values()
    for obj in brands:
        brand_name.append(obj.brand_name)
    brand_name = sorted(brand_name)
    return render_template('index.html', brands=brand_name, obj=brands)


@app.route('/single_model/<model_id>', strict_slashes=False)
def single_model(model_id):
    """The single model page for each device."""
    get_model = storage.get(Model, model_id)
    return render_template('model-single.html', model=get_model)


@app.route('/search', methods=['POST'], strict_slashes=False)
def search():
    """Get the content from the frontend user input."""
    user_data = request.get_json()
    matching_objects = []
    for summary in storage.all(Summary).values():
        obj_dict = summary.to_dict()
        # Check if all key-value pairs in user_data are present in obj_dict
        if all(obj_dict.get(key) == value for key, value in user_data.items()):
            matching_objects.append(summary)
    obj_dict = [obj.to_dict() for obj in matching_objects]
    # result(matching_objects)
    return jsonify(obj_dict)


@app.route('/result', strict_slashes=False)
def result():
    """Get the result from the seach content from the frontend user input."""
    obj_ids = request.args.getlist('model_id')
    obj_list = [storage.get(Model, obj_id) for obj_id in obj_ids]
    return render_template('result.html', result=obj_list)


@app.route('/admin', strict_slashes=False)
def admin():
    """Admin page."""
    br_cnt = storage.count(Brand)
    mo_cnt = storage.count(Model)
    return render_template('admin.html',
                           brand_count=br_cnt,
                           model_count=mo_cnt
                           )

def brand():
    """Brand page."""
    return render_template('brand.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)
