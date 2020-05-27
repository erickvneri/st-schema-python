from marshmallow import Schema, fields
from typing import List
from stschema.interface import DeviceDiscoverySchema, Device
from stschema.base.util import HeadersSchema
from stschema.base.response import BaseResponse


class DiscoveryResponse(BaseResponse):
    """Inherits from the BaseResponse class.
    The DiscoveryResponse class handles the
    final representation of a Discovery
    Response as the ST Schema documentation
    refers:

        :::param devices: a list of devices.
        :::param headers: headers of a request and response"""

    def __init__(self, devices: List[Device], request_id: str):
        BaseResponse.__init__(self, interaction_type='discoveryResponse', request_id=request_id)
        self.devices = devices


class DiscoveryResponseSchema(Schema):
    """The DiscoverySchema handles the
    serialization of the DiscoveryResponse class.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions."""

    devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices'))
    headers = fields.Nested(HeadersSchema, attribute='headers')