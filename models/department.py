from common.db import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    description = db.Column(db.String(300), nullable= False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def get_all_department(cls):
        return cls.query.all()