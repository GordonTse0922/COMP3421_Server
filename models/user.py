
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from common.db import db
from models.post import PostModel

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False )
    email = db.Column(db.String(100), nullable= False, unique = True)
    created_at = db.Column(db.DateTime, nullable= False)
    posts = db.relationship('PostModel')

    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = datetime.now()

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self):
        db.session.commit()

    @classmethod
    def login(cls,email):
        print(email)
        user=cls.query.filter_by(email=email).first()
        return user

    @classmethod
    def get_user(cls):
        userId = request.args.get('id', type = int)
        result=cls.query.filter_by(id=userId).first()
        print(result)
        return cls.query.filter_by(id=userId).first()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def get_all_user(cls):
        return cls.query.all()

