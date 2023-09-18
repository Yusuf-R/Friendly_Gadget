#!/usr/bin/env python3
from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')




from web_dynamic.admin.routes import *