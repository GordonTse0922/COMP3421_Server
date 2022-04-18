from datetime import datetime
from common.db import db
from flask_sqlalchemy import event
from flask import request

class CommentModel(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer,  db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.String(300), nullable= False)
    created_at = db.Column(db.DateTime, nullable= False)

    def __init__(self, user_id, post_id,content):
        self.user_id = user_id
        self.post_id = post_id
        self.content = content
        self.created_at = datetime.now()

    @classmethod
    def get_comments(cls):
        post_id = request.args.get('id', type = int)
        return cls.query.filter_by(post_id=post_id).all()
        

    def add(self):
        db.session.add(self)
        db.session.commit()


# @event.listens_for(DepartmentModel.__table__, 'after_create')
# def create_departments(*args, **kwargs):
#     db.session.add(DepartmentModel(name='Computing', description='Computing department'))
#     db.session.add(DepartmentModel(name='Electrical Engineering', description='Electrical Engineering department'))
#     db.session.commit()