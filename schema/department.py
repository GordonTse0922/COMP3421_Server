from common.ma import ma
from models.department import DepartmentModel

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=DepartmentModel

    id: ma.Str()
    name: ma.Str()
    description = ma.Str()
