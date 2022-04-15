from common.db import db
import datetime

class PostModel (db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(300), nullable= False)
    created_at = db.Column(db.DateTime, nullable= False)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'), nullable=False)
    department_id = db.Column(db.Integer,  db.ForeignKey('departments.id'), nullable=False)

    def __init__(self, title, content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = datetime.now()

    @classmethod
    def get_post(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_post(cls):
        return cls.query.all()

    @classmethod
    def get_all_department_post(cls, id):
        return cls.query.filter_by(department_id=id).all()
