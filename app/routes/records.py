from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('records', __name__, url_prefix='/records')

@bp.route('/new', methods=['GET'])
def new_record():
    """
    新增收支頁面
    - 呼叫 Category.get_all() 取得分類清單
    - 渲染 templates/records/form.html
    """
    pass

@bp.route('', methods=['POST'])
def create_record():
    """
    建立收支
    - 接收表單資料 (date, amount, type, category_id, description)
    - 驗證資料後呼叫 Record.create()
    - 成功重導向至 '/'
    """
    pass

@bp.route('/<int:id>/edit', methods=['GET'])
def edit_record(id):
    """
    編輯收支頁面
    - 根據 id 取得單筆記錄 (Record.get_by_id)
    - 取得分類清單
    - 渲染 templates/records/form.html 並帶入預設值
    """
    pass

@bp.route('/<int:id>/update', methods=['POST'])
def update_record(id):
    """
    更新收支
    - 接收表單資料並驗證
    - 呼叫 Record.update(id, ...)
    - 成功重導向至 '/'
    """
    pass

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_record(id):
    """
    刪除收支
    - 呼叫 Record.delete(id)
    - 成功重導向至 '/'
    """
    pass
