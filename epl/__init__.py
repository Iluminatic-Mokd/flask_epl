# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# app.secret_key = 'sdlflkposkrofkpsldas'

# from epl import models
# from epl.routes import register_blueprints

# register_blueprints(app)

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'sdlflkposkrofkpsldas'
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from epl import models
    from epl.routes import register_blueprints
    register_blueprints(app)

    return app
