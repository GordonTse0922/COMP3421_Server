from common.db import db
from flask_sqlalchemy import event
from flask import request

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.String(300), nullable= False)
    # posts = db.relationship('PostModel')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_department(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_department(cls):
        id = request.args.get('id', type = int)
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_department(cls):
        return cls.query.all()

