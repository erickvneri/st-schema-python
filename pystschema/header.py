from marshmallow import Schema, fields

class Header:
    schema = 'st-schema'
    version = '1.0'

    def __init__(self, interaction_type: str, request_id: str) -> 'Header':
        self.interaction_type = interaction_type
        self.request_id = request_id


class HeadersSchema(Schema):
    schema = fields.Str()
    version = fields.Str()
    interaction_type = fields.Str()
    request_id = fields.Str()
