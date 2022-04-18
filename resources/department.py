from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from models.department import DepartmentModel
from schema.department import DepartmentSchema
from sqlalchemy.exc import IntegrityError

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

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = department_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        name=data['name']
        description=data['description']
        if  name and description :
            department = DepartmentModel(name, description)
            try:
                department.add_department()
            except IntegrityError:
                return {
                'message': 'department already exist!',
                # 'user': user_schema.dump(user)
                }, 400

            return {
                'message': 'Insert department success',
                # 'user': user_schema.dump(user)
            }
        return {"message": "No input data provided"}, 400

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
        # print(departments[0].posts)
        return {
            'message': '',
            'departments': departments_schema.dump(departments)
        }