from epl.routes.main import main_bp
from epl.routes.clubs import clubs_bp
from epl.routes.players import players_bp

def register_blueprints(app):
    """Register all blueprints with the Flask application"""
    app.register_blueprint(main_bp)
    app.register_blueprint(clubs_bp)
    app.register_blueprint(players_bp)
