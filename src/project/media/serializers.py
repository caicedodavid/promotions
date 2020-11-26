from marshmallow import Schema, fields
from marshmallow.validate import Regexp

from project import ma
from .models import Media


class MediaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Media
        load_instance = True


class LoadMediaSchema(Schema):
    data = fields.String(required=True)
    name = fields.String(required=True, validate=Regexp(r'.+\..+'))
    description = fields.String(required=False)
