import os

from flask import Flask
from api.models import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'databse.sqlite'),
    # )


    db.init_app(app)

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
