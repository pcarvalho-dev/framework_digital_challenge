from marshmallow import Schema, fields


class ApiSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)

    class Meta:
        strict = True
        ordered = True