from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
    db.init_app(app)

    # registration of routes
    from .routes.main import main
    from .routes.api import api
    from .routes.pdf import pdf

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(pdf)

    return app