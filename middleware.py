from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

# Initialize the JWT manager

jwt = JWTManager()

# Middleware to protect routes requiring JWT authentication

def jwt_required_view(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        return fn(current_user, *args, **kwargs)
    return wrapper