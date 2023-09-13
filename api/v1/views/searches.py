#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route("/searches",
                 methods=["POST"],
                 strict_slashes=False)
def search():
    try:
        data = request.get_json()  # Get the JSON data from the request

        # Process the data as needed
        # For example, you can perform a database query here

        # Return a response (this is just an example response)
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)})
