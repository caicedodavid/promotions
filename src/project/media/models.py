from sqlalchemy.sql import func

from project import db
from project.mixins import ModelMixin


class Media(db.Model, ModelMixin):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    ext = db.Column(db.String(8), nullable=False)
    description = db.Column(db.String(64), nullable=True)
    url = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=func.now(), nullable=True)
