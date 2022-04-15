from flask_restful import Resource
from marshmallow import ValidationError
from schema.user import UserSchema
from flask import request
from models.user import UserModel

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)
class User (Resource):

    def get(self):
        user = UserModel.get_user()
        if not user:
            return {
                'message': 'user not exist!'
            }, 403
        return {
            'message': '',
            'user': user_schema.dump(user).data
        }

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        user = UserModel(data['name'], data['email'])
        user.add_user()
        return {
            'message': 'Insert user success',
            'user': user_schema.dump(user)
        }

    def put(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422

        user = UserModel.get_user()
        if not user:
            return {
                'message': 'user not exist!'
            }, 403
        user.email = data['email']
        # user.password = data['password']
        return {
            'message': 'Update user success',
            'user': user_schema.dump(user).data
        }

    def delete(self):
        UserModel.delete_user()
        return {
            'message': 'Delete done!'
        }

class Users(Resource):
    def get(self):
        return {
            'message': 'All users',
            'users': UserModel.get_all_user()
        }