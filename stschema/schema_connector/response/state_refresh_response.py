from typing import List
from marshmallow import Schema, fields
from stschema.interface import DeviceStateSchema, Device
from stschema.base.response import BaseResponse
from stschema.base.util import HeadersSchema


class StateResponse(BaseResponse):
    """Inherits from the BaseResponse class.
    The StateResponse class handles the
    representation of the stateRefreshResponse.

        :::param headers"
        :::param device_state"""

    def __init__(self, devices: List[Device], request_id: str, interaction_type: str = 'stateRefreshResponse'):
        BaseResponse.__init__(self, interaction_type=interaction_type, request_id=request_id)
        self.device_state = devices
