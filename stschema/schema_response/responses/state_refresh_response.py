from marshmallow import Schema, fields, pre_dump, post_dump
from stschema.util import HeadersSchema, BaseResponse, AuthenticationSchema
from stschema.schema_device.schemas import DeviceStateSchema, DeviceErrorSchema

from pprint import pprint # Delete line

class StateResponse(BaseResponse):
    """
    Inherits from the BaseResponse class.
    The StateResponse class handles the
    representation of the stateRefreshResponse.

        :::param headers
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

    @pre_dump
    def _verify_dump(self, data, **kwargs):
        # Verify Headers attribute
        if data.headers:
            self.dump_fields.update(
                headers = fields.Nested(HeadersSchema, attribute='headers', required=True)
            )
        # Verify Authentication attribute
        if data.authentication:
            self.dump_fields.update(
                authentication = fields.Nested(AuthenticationSchema, attribute='authentication')
            )
        # Verify State instance attribute
        # If device_error at device instance,
        # DeviceErrorSchema will be used, else
        # DeviceStateSchema will be used.
        if data.device_state:
            if data.device_state[0].device_error:
                self.dump_fields.update(
                    deviceState=fields.List(fields.Nested(DeviceErrorSchema), attribute='device_state')
                )
            else:
                self.dump_fields.update(
                    deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state')
                )
        return data

    @post_dump
    def _reset_device_state(self, data, **kwargs):
        # Reset deviceState to support
        # DeviceStateSchema as default
        # schema.
        self.dump_fields.update(
            deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state')
        )
        return data
