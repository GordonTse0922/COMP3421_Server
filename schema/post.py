from common.ma import ma, must_not_be_blank
from marshmallow import Schema,fields,ValidationError
from models.post import PostModel
from models.user import UserModel
from schema.comment import CommentSchema
from schema.user import UserSchema

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=PostModel

    id= fields.Integer(dump_only=True)
    user_id=fields.Integer(required=True)
    user=fields.Nested(UserSchema(only=['id','name']), many=False,dump_only=True)
    department_id= fields.Integer(required=True,validate=must_not_be_blank)
    title= fields.String(required=True, validate=must_not_be_blank)
    content = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
    # name =fields.String(dump_only=True)
    comments= fields.Nested(CommentSchema(only=['user_id','content']), many=True)
