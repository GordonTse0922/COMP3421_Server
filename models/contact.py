from datetime import datetime
from common.db import db
from flask_sqlalchemy import event

class ContactModel(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable= False)
    feedback = db.Column(db.String(500), nullable= False)
    created_at = db.Column(db.DateTime, nullable= False)

    def __init__(self, name, email, feedback):
        self.name = name
        self.email = email
        self.feedback = feedback
        self.created_at = datetime.now()

    def add_feedback(self):
        db.session.add(self)
        db.session.commit()