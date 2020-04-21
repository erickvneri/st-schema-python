from marshmallow import Schema, fields

class Header:
    """The HeaderClass is used by the
    Response constructor.
        :::param interaction_type: parameter
        acquired at incoming ST Requests.
        :::param request_id: parameter
        acquired at incoming ST Requests."""

    schema = 'st-schema'
    version = '1.0'

    def __init__(self, interaction_type: str, request_id: str) -> 'Header':
        self.interaction_type = interaction_type
        self.request_id = request_id


class HeadersSchema(Schema):
    """The HeaderSchema handles the
    serialization of the Header class.
    It parses the Snake Cased attributes
    into Camel Case attributes as specified
    in the ST-Scema documentation."""

    schema = fields.Str()
    version = fields.Str()
    interactionType = fields.Field(attribute='interaction_type')
    requestId = fields.Field(attribute='request_id')