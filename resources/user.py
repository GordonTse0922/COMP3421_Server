from flask_restful import Resource
from schema.user import UserSchema, CreateUserSchema
from flask import request
from models.user import UserModel

createUser_schema = CreateUserSchema()
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
        result = user_schema.load(request.json)
        user = UserModel(result['name'], result['email'])
        user.add_user()
        return {
            'message': 'Insert user success',
            'user': user_schema.dump(user)
        }

    def put(self):
        result = user_schema.load(request.json)
        if len(result.errors) > 0:
            return result.errors, 433
        user = UserModel.get_user()
        if not user:
            return {
                'message': 'user not exist!'
            }, 403
        user.email = result.data['email']
        user.password = result.data['password']
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