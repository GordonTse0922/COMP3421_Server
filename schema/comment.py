from common.ma import ma, must_not_be_blank
from marshmallow import Schema,fields,ValidationError
from models.comment import CommentModel
from schema.user import UserSchema

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=CommentModel

    id= fields.Integer(dump_only=True)
    user_id=fields.Integer(required=True)
    post_id= fields.Integer(required=True,validate=must_not_be_blank)
    content = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
    user=fields.Nested(UserSchema(only=['id','name']), many=False,dump_only=True)

class CommentOutputSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=CommentModel

    id= fields.Integer(dump_only=True)
    # user_id=fields.Integer(required=True)
    post_id= fields.Integer(required=True,validate=must_not_be_blank)
    content = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
    user=fields.Nested(UserSchema(only=['id','name']), many=False)
