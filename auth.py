from flask import request, jsonify
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != "Bearer SECRET_TOKEN":
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorator
