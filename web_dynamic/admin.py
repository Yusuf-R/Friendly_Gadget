#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""

from models.brand import Brand
from models.model import Model
from flask import Flask, abort, render_template, request, flash, json
import requests
from models import storage
import os

secret_key = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/', strict_slashes=False)
@app.route('/admin', strict_slashes=False)
def admin():
    """Admin page."""
    br_cnt = storage.count(Brand)
    mo_cnt = storage.count(Model)
    return render_template('admin.html',
                           brand_count=br_cnt,
                           model_count=mo_cnt
                           )


@app.route('/brands', strict_slashes=False)
def brands():
    """Brand page."""
    url = "http://0.0.0.0:5100/api/v1/brands"
    data = requests.get(url)
    if data.status_code == 200:
        brands = data.json()
        return render_template('brands.html', brands=brands)
    else:
        abort(404)
        

@app.route('/models', strict_slashes=False)
def models():
    """Brand page."""
    obj = storage.all(Model).values()
    return render_template('models.html', obj=obj)



@app.route('/add_brand', methods=['POST', 'GET'], strict_slashes=False)
def add_brand():
    """Create a brand."""
    if request.method == 'GET':
        return render_template('add_brand.html')
    if request.method == 'POST':
        br_name = request.form.get('name')
        url = "http://0.0.0.0:5100/api/v1/brands"
        headers = {'Content-Type': 'application/json'}
        params = {'brand_name': br_name}
        response = requests.post(url, headers=headers, json=params)
        if response.status_code == 201:
            flash(f"Brand '{br_name}' successfully added!", 'success')
            return render_template('add_brand.html')
        else:
            abort(500)
    else:
        abort(404)


# @app.route('/edit_brand/<brand_id>', methods=['PUT'], strict_slashes=False)
# def edit_brand(brand_id):
#     """Edit a brand."""
#     url = "http://0.0.0.0:5100/api/v1/brands/{}".format(brand_id)
#     header = {'Content-Type': 'application/json'}
#     data = request.get_json()
#     print(data)
#     response = requests.put(url, headers=header, json=data)
#     if response.status_code == 200:
#         flash(f"Brand '{data['brand_name']}' successfully edited!", 'success')
#         return render_template('edit_brand.html')
#     else:
#         abort(500)


@app.route('/edit_brand/<brand_id>', strict_slashes=False)
def edit_brand(brand_id):
    """Edit a brand."""
    get_brand = storage.get(Brand, brand_id)
    return render_template('edit_brand.html', brand=get_brand)
  
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
