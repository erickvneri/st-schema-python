from marshmallow import Schema, fields


class BaseHeaders:
    """
    The BaseHeaders represents the
    communication metadata between a
    third-party Cloud and the SmartThings
    Cloud. 'schema' and 'version' attributes
    are default class values:
        schema = 'st-schema'
        version = '1.0'

        :::param interaction_type
        :::param request_id
    """

    schema = 'st-schema'
    version = '1.0'

    def __init__(self, interaction_type: str, request_id: str) -> 'BaseHeaders':
        self.interaction_type = interaction_type
        self.request_id = request_id

class HeadersSchema(Schema):
    """
    The HeaderSchema handles the
    serialization of the BaseHeaders
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    schema = fields.Str()
    version = fields.Str()
    interactionType = fields.Str(attribute='interaction_type')
    requestId = fields.Str(attribute='request_id')
