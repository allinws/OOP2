from flask import Blueprint, request, jsonify
from ..services.category_service import CategoryService

bp = Blueprint('categories', __name__)

# list categories
@bp.route('/categories/', methods=["GET"])
def get_all_categories():
    category_service = CategoryService()
    categories = category_service.get_all()
    category_dicts = [category.to_dict() for category in categories]
    return jsonify(category_dicts), 200


@bp.route('/categories/', methods=["POST"])
def create_category():
    category_service = CategoryService()
    name = request.form['name']
    category = category_service.create(name=name)
    category_dict = category.to_dict()
    return jsonify(category_dict), 201

@bp.route('/categories/<int:category_id>/', methods=["PUT"])
def update_category(category_id):
    category_service = CategoryService()
    name = request.form.get('name')
    category = category_service.update(category_id=category_id, name=name)
    if category:
        category_dict = category.to_dict()
        return jsonify(category_dict), 200
    else:
        return 'Category not found', 404

@bp.route('/categories/<int:category_id>/', methods=["DELETE"])
def delete_category(category_id):
    category_service = CategoryService()
    result = category_service.delete(category_id=category_id)
    if result:
        return result, 200
    else:
        return 'Category not found', 404