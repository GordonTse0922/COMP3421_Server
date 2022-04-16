from flask_restful import Resource
from flask import request
from models.user import UserModel
from schema.user import UserSchema
from marshmallow import ValidationError


user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)
class Auth(Resource):
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


