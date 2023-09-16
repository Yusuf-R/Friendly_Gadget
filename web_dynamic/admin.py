#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""

from models.brand import Brand
import json
from models.model import Model
from models.summary import Summary
from flask import Flask, abort, render_template, request, flash, jsonify, redirect, url_for
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
    """Render the Brand page."""
    url = "http://0.0.0.0:5100/api/v1/brands"
    data = requests.get(url)
    if data.status_code == 200:
        brands = data.json()
        return render_template('brands.html', brands=brands)
    else:
        abort(404)
        
@app.route('/add_brand', methods=['POST', 'GET'], strict_slashes=False)
def add_brand():
    """Create a new instance of brand."""
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
            return brands()
        else:
            flash(f"Brand '{br_name}' already exists!", 'danger')
            return render_template('add_brand.html')
    else:
        abort(404)


@app.route('/edit_brand/<brand_id>', strict_slashes=False)
def edit_brand(brand_id):
    """Render the EditPage to enable editing of the ginven instance."""
    get_brand = storage.get(Brand, brand_id)
    return render_template('edit_brand.html', brand=get_brand)
  

@app.route('/update_brand/<brand_id>', methods=['POST'], strict_slashes=False)
def update_brand(brand_id):
    """Editing a brand and send this update to the database using API."""
    data = request.form.get('name')
    print("The edit data is: ", data)
    url = "http://0.0.0.0:5100/api/v1/brands/{}".format(brand_id)
    headers = {'Content-Type': 'application/json'}
    params = {'brand_name': data}
    response = requests.put(url, headers=headers, json=params)
    print(response.status_code)
    if response.status_code == 200:
        flash(f"Brand '{data}' successfully updated!", 'success') 
        print("Inside the IF")       
        # return redirect(url_for('add_brand'))
        return brands()
    else:
        abort(500)


@app.route('/delete_brand/<brand_id>', methods=['GET'], strict_slashes=False)
def delete_brand(brand_id):
    """Delete an object instance of the brand."""
    url = "http://0.0.0.0:5100/api/v1/brands/{}".format(brand_id)
    obj = storage.get(Brand, brand_id)
    response = requests.delete(url)
    storage.save()
    if response.status_code == 200:
        flash(f"Brand '{obj.brand_name }' successfully deleted!", 'success')
        return brands()
    else:
        abort(500)


@app.route('/models', strict_slashes=False)
def models():
    """Render the Model page."""
    obj = storage.all(Model).values()
    return render_template('models.html', obj=obj)

@app.route('/add_model', strict_slashes=False)
def add_model():
  """ Render the model page for Adding a new obj insance"""
  all_brand_obj = storage.all(Brand).values()  
  return render_template('add_model.html', brands=all_brand_obj)


@app.route('/create_model', methods=['POST'], strict_slashes=False)
def create_model():
  """Get the properties of this new obj instance of Model create this obj via API"""
  model_name = request.form['model_name']
  model_img = request.form['img_url']
  brand_id = request.form['brand']  
  url = "http://0.0.0.0:5100/api/v1/brands/{}/models".format(brand_id)
  headers = {'Content-Type': 'application/json'}
  params = {'model_name': model_name, 'model_img': model_img}
  response = requests.post(url, headers=headers, json=params)
  if response.status_code == 201:
    flash(f"Model '{model_name}' successfully added!", 'success')
    return models()
  else:
    flash(f"Model '{model_name}' already exists!", 'danger')
    return models()


@app.route('/edit_model/<model_id>', strict_slashes=False)
def edit_model(model_id):
  """Render the edit page with necessary information to Edit a model."""
  get_model = storage.get(Model, model_id)
  return render_template('edit_model.html', model=get_model)


@app.route('/update_model/<model_id>', methods=['POST'], strict_slashes=False)
def update_model(model_id):
  """Edit a model and send this update to the database using API."""
  model_name = request.form['model_name']
  model_img = request.form['img_url']
  data = {'model_name': model_name, 'model_img': model_img}
  url = "http://0.0.0.0:5100/api/v1/models/{}".format(model_id)
  headers = {'Content-Type': 'application/json'}
  params = {'model_name': model_name, 'model_img': model_img}
  response = requests.put(url, headers=headers, json=params)
  print(response.status_code)
  if response.status_code == 200:
    flash(f"Model '{model_name}' successfully updated!", 'success')       
    # return redirect(url_for('add_brand'))
    return models()
  else:
    abort(500)

  
@app.route('/delete_model/<model_id>', methods=['GET'], strict_slashes=False)
def delete_model(model_id):
  """Delete a model."""
  url = "http://0.0.0.0:5100/api/v1/models/{}".format(model_id)
  obj = storage.get(Model, model_id)
  response = requests.delete(url)
  storage.save()
  if response.status_code == 200:
    flash(f"Model '{obj.model_name }' successfully deleted!", 'success')
    return models()
  else:
    abort(500)


@app.route('/summaries', strict_slashes=False)
def summaries():
    """Render the Summary page."""
    obj = storage.all(Model).values()
    return render_template('summaries.html', obj=obj)

@app.route('/view_summary/<model_id>', methods=['GET'], strict_slashes=False)
def view_summary(model_id):
  """Renders the view summary of a particular model object"""
  obj = storage.get(Model, model_id)
  return render_template('view_summary.html', models=obj)


@app.route('/add_summary/<model_id>', methods=['GET'], strict_slashes=False)
def add_summary(model_id):
  """Renders the add summary page for a particular model object"""
  obj = storage.get(Model, model_id)
  return render_template('add_summary.html', models=obj)


@app.route('/create_summary/<model_id>', methods=['POST'], strict_slashes=False)
def create_summary(model_id):
  """Gets the properties of this new obj instance of Summary and sends this to the API to create this obj instance"""  
  data = request.form.get('summaryData')
  url = "http://0.0.0.0:5100/api/v1/models/{}/summaries".format(model_id)
  obj = storage.get(Model, model_id)
  if obj is None:
    abort("invalid model id"), 400
  headers = {'Content-Type': 'application/json'}
  # convert data to JSON
  data = eval(data)
  if type(data) != dict:
    abort("Data must be in JSON format"), 400
  response = requests.post(url, headers=headers, json=data)
  if response.status_code == 201:
    flash(f"Summary for model '{obj.model_name}' successfully added!", 'success')
    return summaries()
  else:
    flash(f"Summary for model '{obj.model_name}' already exists!", 'danger')
    return summaries()
  

@app.route('/edit_summary/<model_id>', strict_slashes=False)
def edit_summary(model_id):
  """Render the edit page with necessary information to Edit a summary."""
  obj = storage.get(Model, model_id)
  return render_template('edit_summary.html', models=obj)


@app.route('/update_summary/<model_id>', methods=['POST'], strict_slashes=False)
def update_summary(model_id):
  """Implement the necessary update on an obj base on the dicinoary of data."""
  data = request.form.get('summaryData')
  summary_id = [obj.id for obj in storage.get(Model, model_id).summaries][0]
  url = "http://0.0.0.0:5100/api/v1/summaries/{}".format(summary_id)
  obj = storage.get(Model, model_id)
  if obj is None:
    abort("invalid model id"), 400
  headers = {'Content-Type': 'application/json'}
  # convert data to JSON
  data = eval(data)
  if type(data) != dict:
    abort("Data must be in JSON format"), 400
  response = requests.put(url, headers=headers, json=data)
  if response.status_code == 200:
    flash(f"Summary for model '{obj.model_name}' successfully updated!", 'success')
    return summaries()
  else:
    abort(500)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
