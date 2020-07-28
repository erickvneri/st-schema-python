from marshmallow import Schema, fields
from stschema.util import HeadersSchema, BaseResponse
from stschema.schema_device.schemas import DeviceStateSchema, DeviceErrorSchema


class StateResponse(BaseResponse):
    """
    Inherits from the BaseResponse class.
    The StateResponse class handles the
    representation of the stateRefreshResponse.

        :::param headers"
        :::param device_state
    """

    def __init__(self, devices: list, request_id: str, interaction_type: str = 'stateRefreshResponse'):
        BaseResponse.__init__(self, interaction_type=interaction_type, request_id=request_id)
        self.device_state = devices


class StateRefreshResponseSchema(Schema):
    """
    The StateRefreshResponseSchema handles
    the serialization of the StateResponse
    class supporting the nested
    DeviceStateSchema, HeadersSchema and
    DeviceErrorSchema (dynamicly handled).
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    headers = fields.Nested(HeadersSchema, attribute='headers')
    deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state')

    def __init__(self, **state_info):
        Schema.__init__(self)
        self.states = state_info.get('states')
        if self.states:
            for state in self.states:
                if state.device_error:
                    self.dump_fields.update(
                        deviceState=fields.List(fields.Nested(DeviceErrorSchema), attribute='device_state')
                    )
