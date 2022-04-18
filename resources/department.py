from flask_restful import Resource
from flask import request
from models.department import DepartmentModel
from schema.department import DepartmentSchema

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)
class Department(Resource):
    def get(self):
        department =DepartmentModel.get_department()
        if not department:
            return {
                'message': 'department not exist!'
            }, 403
        return {
            'message': '',
            'departments': department_schema.dump(department)
        }, 200

    def post(self, name):
        return {'post': name}

    def put(self, name):
        return {'post': name}

    def delete(self, name):
        return {'post': name}


class Departments(Resource):
    def get(self):
        departments =DepartmentModel.get_all_department()
        print(departments)
        if not departments:
            return {
                'message': 'No department in DB'
            }, 403
        print(departments[0].posts)
        return {
            'message': '',
            'departments': departments_schema.dump(departments)
        }