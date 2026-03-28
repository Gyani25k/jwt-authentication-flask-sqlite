
from flask import request,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Custom middleware to protect routes
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200