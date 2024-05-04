from flask import Blueprint, jsonify
from flask import current_app as app


similar_bp = Blueprint(
    'similar_bp', __name__
)

@similar_bp.route("/similar")
def get_similar():
    return jsonify({ 'status': "success" }), 201,