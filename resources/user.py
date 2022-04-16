from sqlite3 import IntegrityError
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from schema.user import UserLoginSChema, UserSchema
from flask import request, jsonify
from models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

user_schema = UserSchema(many=False)
login_schema=UserLoginSChema(many=False)
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
        password=data['password']
        username=data['name']
        email=data['email']
        if username and password and email:
            user = UserModel(username, email, generate_password_hash(password))
            try:
                user.add_user()
            except IntegrityError:
                return {
                'message': 'username/email already exist!',
                # 'user': user_schema.dump(user)
                }, 400

            return {
                'message': 'Insert user success',
                # 'user': user_schema.dump(user)
            }
        return {"message": "No input data provided"}, 400

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

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = login_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        password=data['password']
        email=data['email']
        user=UserModel.get_user(email)
        if check_password_hash(user.password,password) and user is not None:
            return {
                'meesage': 'Login success'
            }, 200
        else:
            return {
                'meesage': 'Incorrect Email/Password'
            }, 400


