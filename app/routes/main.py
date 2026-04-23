from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    首頁：顯示目前總餘額與近期的收支紀錄
    - 呼叫 Record.get_balance_summary() 取得餘額
    - 呼叫 Record.get_all() 取得列表
    - 渲染 templates/index.html
    """
    pass

@bp.route('/statistics')
def statistics():
    """
    金錢流向統計頁：顯示特定期間的收支統計數據
    - 呼叫相關 Model 統計方法
    - 渲染 templates/statistics.html
    """
    pass
