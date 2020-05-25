from marshmallow import Schema, fields


class BaseHeaders(object):
    """The BaseHeaders handles the
    metadata of the communication
    between the Schema Connector and
    the SmartThings Cloud.
        :::param interaction_type
        :::param request_id"""

    schema = 'st-schema'
    version = '1.0'

    def __init__(self, interaction_type: str, request_id: str):
        self.interaction_type = interaction_type
        self.request_id = request_id


class HeadersSchema(Schema):
    """The HeaderSchema handles the
    serialization of the BaseHeaders class.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions."""

    schema = fields.Str()
    version = fields.Str()
    interactionType = fields.Str(attribute='interaction_type')
    requestId = fields.Str(attribute='request_id')
