from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        strict = True
        ordered = True