#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from flask import Flask, render_template
import os
from models import storage
from models.brand import Brand
from models.model import Model
from web_dynamic.admin import admin_bp


app = Flask(__name__)
secret_key = os.urandom(32)
app.config['SECRET_KEY'] = secret_key


app.register_blueprint(admin_bp)



@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5802, debug=True)
