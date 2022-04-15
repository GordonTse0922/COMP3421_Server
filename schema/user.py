from common.ma import ma

class UserSchema(ma.Schema):
    name: ma.Str(required=True)
    email = ma.Email(required=True)
    create_at = ma.DateTime(required=True)