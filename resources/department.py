from flask_restful import Resource
from flask import request
from models.department import DepartmentModel

class Department(Resource):
    def get(self, id ):
        post =DepartmentModel.get(id)
        if not post:
            return {
                'message': 'post not exist!'
            }, 403
        return {
            'message': '',
            'post':'testing'
        }

    def post(self, name):
        return {'post': name}

    def put(self, name):
        return {'post': name}

    def delete(self, name):
        return {'post': name}


class Departments(Resource):
    def get(self):
        departments =DepartmentModel.get_all_department()
        if not departments:
            return {
                'message': 'No department in DB'
            }, 403
        return {
            'message': '',
            'post':'testing'
        }