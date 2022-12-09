from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from turbo_flask import Turbo

from models import models

turbo = Turbo()
# Factory function


def create_app():
    app = Flask(__name__)
    turbo.init_app(app)


    app.config['SECRET_KEY'] = "asdfljkhlkuagh987342yr978uifdhnbcvxa86g"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webtools:PASSword01!@localhost:5432/parquet'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        return render_template('home/index.html')

    @app.route('/about')
    def about():
        return render_template('about/about.html')

    from . import breadcrumb
    app.register_blueprint(breadcrumb.bp)

    return app
