from typing import List
from marshmallow import Schema, fields
from stschema.interface import DeviceStateSchema, Device
from stschema.responses.util import Header, HeadersSchema


class StateResponse(object):
    """The StateResponse class will handle the
    final representation of a State Refresh
    Response as the ST Schema documentation
    refers:

        :::param device_state: a list of devices
        specifying the current state of each capability.
        :::param headers: headers or a request and response"""

    def __init__(self, devices: List[Device], request_id):
        self.device_state = devices
        self.headers = Header(interaction_type='stateRefreshResponse', request_id=request_id)


class StateRefreshResponseSchema(Schema):
    """The StateRefreshResponseSchema will return
    a StateRefresh Response JSON as it is referred
    at the ST Schema documentation.

        :::param deviceState:
            [{
                externalDeviceId,
                deviceCookie
                states: [{state}...]
            }]
        :::param headers: dict with JSON
        headers inherited from ST response."""

    headers = fields.Nested(HeadersSchema, attribute='headers')
    deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state')


