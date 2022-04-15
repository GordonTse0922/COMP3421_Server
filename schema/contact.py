from common.ma import ma, must_not_be_blank
from models.contact import ContactModel
from marshmallow import Schema,fields,ValidationError

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=ContactModel

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=must_not_be_blank)
    email = fields.Email(required=True, validate=must_not_be_blank)
    feedback = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)