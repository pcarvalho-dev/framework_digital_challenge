from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String(required=True)
    username = fields.String(required=True)

    class Meta:
        strict = True
        ordered = True