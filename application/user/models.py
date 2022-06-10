import re
from application.common.models.base_model import BaseModel
from extensions import db
from passlib.handlers.pbkdf2 import pbkdf2_sha256


class User(db.Model, BaseModel):
    __tablename__ = "user"

    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)[20:]

    def check_password(self, candidate):
        return pbkdf2_sha256.verify(candidate, f"$pbkdf2-sha256$29000{self.password}")

    def create_fields(self, request_body):
        self.email = request_body.get("email", self.email)
        self.username = request_body.get("username", self.username)
        self.set_password(request_body["password"])
        
        return self

    def update_fields(self, request_body):
        self.email = request_body.get("email", self.email)
        self.username = request_body.get("username", self.username)
        if "password" in request_body:
            self.set_password(request_body["password"])

        return self
