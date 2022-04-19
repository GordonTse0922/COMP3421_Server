import os

from flask import Config, Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from resources.comment import Comment, Comments
from resources.department import Department, Departments
from resources.post import Post, Posts
from resources.user import Login, User, Users
from resources.contact import Contact
from common.ma import ma
from flask_sqlalchemy import SQLAlchemy
from common.db import db, migrate
from flask_cors import CORS

def create_app():
    # create and configure the app\
    # config_object = Config()
    app = Flask(__name__)
    CORS(app)
    # CORS(app,
    #     origins=[config_object.CORS_ALLOW_ORIGIN], # the domains allowed to access the server
    #     supports_credentials=config_object.CORS_SUPPORTS_CREDENTIALS) # True
    # app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api=Api(app)
    api.add_resource(User, "/user")
    api.add_resource(Login,"/login")
    api.add_resource(Users,"/users")
    api.add_resource(Post,"/post")
    api.add_resource(Posts,"/posts")
    api.add_resource(Department,"/department")
    api.add_resource(Departments,"/departments")
    api.add_resource(Comment,"/comment")
    api.add_resource(Comments,"/comments")
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
