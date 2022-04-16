import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from resources.comment import Comment, Comments
from resources.department import Departments
from resources.post import Post, Posts
from resources.user import Login, User, Users
from resources.contact import Contact
from common.ma import ma
from flask_sqlalchemy import SQLAlchemy
from common.db import db, migrate
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api=Api(app)
    api.add_resource(User, "/user")
    api.add_resource(Login,"/login")
    api.add_resource(Users,"/users")
    api.add_resource(Post,"/post")
    api.add_resource(Posts,"/posts/<int:department_id>")
    api.add_resource(Departments,"/departments")
    api.add_resource(Comment,"/comment")
    api.add_resource(Comments,"/comments/<int:post_id>")
    api.add_resource(Contact, "/contact")
    db.init_app(app)
    migrate.init_app(app,db)
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
