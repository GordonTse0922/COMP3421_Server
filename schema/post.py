from common.ma import ma, must_not_be_blank
from marshmallow import Schema,fields,ValidationError
from models.post import PostModel

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=PostModel

    id= fields.Integer(dump_only=True)
    user_id=fields.Integer(required=True)
    department_id= fields.Integer(required=True,validate=must_not_be_blank)
    title= fields.String(required=True, validate=must_not_be_blank)
    content = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
