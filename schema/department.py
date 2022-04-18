from common.ma import ma, must_not_be_blank
from models.department import DepartmentModel
from marshmallow import Schema,fields,ValidationError

from schema.post import PostSchema

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=DepartmentModel

    id: fields.Integer(dump_only=True)
    name: fields.String(required=True, validate=must_not_be_blank)
    description = fields.String(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
    # posts = fields.Nested(PostSchema(many=True))
