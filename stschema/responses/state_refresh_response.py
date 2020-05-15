from typing import List
from marshmallow import Schema, fields
from stschema.interface import DeviceStateSchema, Device
from stschema.base.response import BaseResponse, HeadersSchema


class StateResponse(BaseResponse):
    """Inherits from the BaseResponse class.
    The StateResponse class handles the final
    representation of a State Refresh Response
    as the ST Schema documentation refers:

        :::param device_state: a list of devices
        specifying the current state of each capability.
        :::param headers: headers or a request and response"""

    def __init__(self, devices: List[Device], request_id: str, interaction_type: str = 'stateRefreshResponse'):
        BaseResponse.__init__(self, interaction_type=interaction_type, request_id=request_id)
        self.device_state = devices


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


