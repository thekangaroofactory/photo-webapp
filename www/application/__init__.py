from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin, AdminIndexView


# declare database
db = SQLAlchemy()

# declare login manager
login_manager = LoginManager()

# declare admin
admin = Admin(name='My App', index_view=AdminIndexView(
    name='Home',
    template='myhome.html',
    url='/admin'))


def create_app():

    # Create app
    app = Flask(__name__)

    # Configurations
    app.config.from_pyfile('../config.py')

    # Init plugins
    db.init_app(app)
    login_manager.init_app(app)

    # Init admin
    admin.init_app(app)

    with app.app_context():

        # Import and register blueprint
        from base.routes import base_bp
        app.register_blueprint(base_bp)

        # Import and register blueprint
        from auth.routes import auth_bp
        app.register_blueprint(auth_bp)

        # Import and register blueprint
        from member.routes import member_bp
        app.register_blueprint(member_bp)

        # Import and register blueprint
        from admin.routes import admin_bp
        app.register_blueprint(admin_bp)

        # Import and register blueprint
        from order.routes import order_bp
        app.register_blueprint(order_bp)

        # create sql tables
        db.create_all()

    return app




