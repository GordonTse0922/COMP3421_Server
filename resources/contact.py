from flask_restful import Resource
from flask import request
from models.contact import ContactModel
from schema.contact import ContactSchema
from marshmallow import ValidationError

contact_schema = ContactSchema(many=False)

class Contact(Resource):
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        try:
            data = contact_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        comment = ContactModel(
            data['name'],
            data['email'],
            data['feedback']
            )
        comment.add_feedback()
        return {
            'message': 'Insert feedback success',
            'feedback': contact_schema.dump(comment)
        }