from marshmallow import Schema, fields
from typing import List
from stschema.interface import DeviceDiscoverySchema, Device
from stschema.responses.util import HeadersSchema, Header


class DiscoveryResponse(object):
    """The DiscoveryResponse class will handle the
    final representation of a Discovery Response as
    the ST Schema documentation refers.

        :::param devices: a list of devices.
        :::param headers: headers of a request and response"""

    headers = None

    def __init__(self, devices: List[Device], request_id: str):
        self.devices = devices
        self.headers = Header(interaction_type='discoveryResponse', request_id=request_id)


class DiscoveryResponseSchema(Schema):
    """The DiscoverySchema class will returns
    a DiscoveryResponse JSON as it is referred
    at the ST Schema documentation.

        :::param devices: [devices]
        :::param headers: dict with JSON
        headers inherited from ST response."""

    devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices'))
    headers = fields.Nested(HeadersSchema, attribute='headers')
