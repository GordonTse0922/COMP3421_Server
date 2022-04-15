import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from resources.department import Departments
from resources.post import Post, Posts
from resources.user import User, Users
from common.ma import ma
from flask_sqlalchemy import SQLAlchemy
from common.db import db
from flask_migrate import Migrate

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api=Api(app)
    api.add_resource(User, "/user/<string:name>")
    api.add_resource(Users,"/users")
    api.add_resource(Post,"/post/<int:id>")
    api.add_resource(Posts,"/posts/<int:department_id>")
    api.add_resource(Departments,"/departments")
    db.init_app(app)
    ma.init_app(app)

    @app.route('/')
    def index():
    # Create data
        db.create_all()
        return 'ok'
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    return app
