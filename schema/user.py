from common.ma import ma, must_not_be_blank
from models.user import UserModel
from marshmallow import Schema,fields,ValidationError

class CreateUserSchema(Schema):
    id: fields.Integer(dump_only=True)
    name: fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True, validate=must_not_be_blank)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=UserModel

    id: fields.Integer(dump_only=True)
    name: fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
