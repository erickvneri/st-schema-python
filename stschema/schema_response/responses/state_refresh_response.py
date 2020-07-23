from marshmallow import Schema, fields
from stschema.schema_device.schemas import DeviceStateSchema, DeviceErrorSchema
from stschema.util import HeadersSchema, BaseResponse


class StateResponse(BaseResponse):
    """Inherits from the BaseResponse class.
    The StateResponse class handles the
    representation of the stateRefreshResponse.

        :::param headers"
        :::param device_state"""

    def __init__(self, devices: list, request_id: str, interaction_type: str = 'stateRefreshResponse'):
        BaseResponse.__init__(self, interaction_type=interaction_type, request_id=request_id)
        self.device_state = devices


class StateRefreshResponseSchema(Schema):
    """The StateRefreshResponseSchema handles
    the serialization of the StateResponse class.
    If the state declared corresponds to a Device
    Error State, the Schema will be dynamically
    updated.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions."""

    headers = fields.Nested(HeadersSchema, attribute='headers')
    deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state')

    def __init__(self, **states):
        Schema.__init__(self)
        self.states = states.get('states')
        if self.states:
            for state in self.states:
                if state.device_error:
                    self.dump_fields.update(
                        deviceState=fields.List(fields.Nested(DeviceErrorSchema), attribute='device_state')
                    )
