from datetime import datetime

from extensions import db
from flask_sqlalchemy import Model


class BaseModel(Model):
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = db.Column(db.DateTime)

    @classmethod
    def get_by_id(cls, record_id):
        return cls.query.get(int(record_id))
