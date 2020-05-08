from .util import BaseHeaders


class BaseResponse(object):
    """The base response will serve as interface
    to create cleaner Response instances.
    It is instancing the BaseHeaders class which
    handles the persistence values such as the
    request Id and the interaction type."""

    devices = []
    device_state = []

    def __init__(self, interaction_type: str, request_id: str):
        self.headers = BaseHeaders(interaction_type=interaction_type, request_id=request_id)


from marshmallow import Schema, fields
from .util import HeadersSchema


class TestSchema(Schema):
    headers = fields.Nested(HeadersSchema, attribute='headers')