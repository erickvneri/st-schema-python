from marshmallow import Schema, fields
from pystschema.interface import DiscoveryDeviceSchema
from pystschema.base import HeadersSchema, Header

class DiscoveryResponse:
    """The DiscoveryResponse class will handle the
    final representation of a Discovery Response as
    the ST Schema documentation refers.
        :::param devices: a list of devices.
        :::param headers: headers or a request and response"""

    headers = None
    devices = []

    def __init__(self, **devices):
        self.devices.append(devices.get('devices'))

    def handle_request(self, request: dict):
        # FIXME: THIS IS JUST A TEST METHOD - PLEASE, IMPLEMENT PROPERLY
        """This method is just a test implementation
        of what the CloudConnector class will have.
        DiscoveryResponse class will only receive devices"""

        request_id = request.get('requestId')
        interaction_type = 'discoveryResponse'
        self.headers = Header(interaction_type=interaction_type, request_id=request_id)

class DiscoverySchema(Schema):
    """The DiscoverySchema class will returns
    a DiscoveryResponse JSON as it is referred
    at the ST Schema documentation.
        :::param devices: [devices]
        :::param headers: dict with JSON
        headers inherited from ST request."""

    devices = fields.List(fields.Nested(DiscoveryDeviceSchema, attribute='devices'))
    headers = fields.Nested(HeadersSchema, attribute='headers')
