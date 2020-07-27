from marshmallow import Schema, fields

class PlanetSchema(Schema):
    id = fields.String(required=False)
    name = fields.String(required=True)
    terrain = fields.String(required=True)
    climate = fields.String(required=True)
    appearances = fields.Int(required=False)