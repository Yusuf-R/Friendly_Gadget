#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from models.brand import Brand
from models.model import Model
from flask import Flask,  render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/', strict_slashes=False)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
