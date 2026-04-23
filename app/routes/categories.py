from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('', methods=['GET'])
def list_categories():
    """
    分類管理頁面
    - 呼叫 Category.get_all()
    - 渲染 templates/categories/index.html
    """
    pass

@bp.route('', methods=['POST'])
def create_category():
    """
    新增分類
    - 接收表單資料 (name, type)
    - 呼叫 Category.create()
    - 重導向至 '/categories'
    """
    pass
