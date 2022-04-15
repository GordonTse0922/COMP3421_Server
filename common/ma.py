from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

ma = Marshmallow()

# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError("Data not provided.")