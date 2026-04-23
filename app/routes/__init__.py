from .main import bp as main_bp
from .records import bp as records_bp
from .categories import bp as categories_bp

def register_blueprints(app):
    """將所有的 Blueprint 註冊到 Flask app"""
    app.register_blueprint(main_bp)
    app.register_blueprint(records_bp)
    app.register_blueprint(categories_bp)
