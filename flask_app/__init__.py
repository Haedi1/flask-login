"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit, Namespace
from uuid import uuid4
import random, string
from sqlalchemy import exists, case, distinct
from flask_moment import Moment

db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()
socketio = SocketIO()
moment = Moment()


def create_app():
    """Construct the core flask_session_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")


    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)
    # socketio.init_app(app)
    # moment.init_app(app)

    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
    )

    # response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets, compile_auth_assets

        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create static asset bundles
        compile_static_assets(app)
        compile_auth_assets(app)

        # Create Database Models
        db.create_all()

        return app
