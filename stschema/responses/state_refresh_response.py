from typing import List
from marshmallow import Schema, fields
from stschema.interface import DeviceStateSchema, Device
from stschema.responses.util import Header, HeadersSchema


class StateRefresh(object):
    """"""
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
    deviceState = fields.Nested(DeviceStateSchema, attribute='device_state')


