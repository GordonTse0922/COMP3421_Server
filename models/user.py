
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from common.db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable= False, unique = True)
    created_at = db.Column(db.DateTime, nullable= False)
    posts = db.relationship('PostModel')

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self):
        db.session.commit()

    @classmethod
    def get_user(cls, name):
        return cls.query.filter_by(name=name).first()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def get_all_user(cls):
        return cls.query.all()

