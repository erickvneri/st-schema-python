from marshmallow import Schema, fields, pre_dump
from stschema.schema_device.schemas import DeviceDiscoverySchema
from stschema.util import BaseResponse, HeadersSchema


class DiscoveryResponse(BaseResponse):
    """
    The DiscoveryResponse is an object
    representation in response to the
    "discoveryRequest" Interaction Type.
    Inherits from BaseResponse.

        :::param devices
        :::param request_id
    """

    def __init__(self, devices: list, request_id: str, interaction_type: str='discoveryResponse') -> 'DiscoveryResponse':
        BaseResponse.__init__(self, interaction_type=interaction_type, request_id=request_id)
        self.devices = devices


class DiscoveryResponseSchema(Schema):
    """
    The DiscoveryResponseSchema handles
    the serialization of the DiscoveryResponse
    class supporting the nested
    DeviceDiscoverySchema, HeadersSchema,
    and AuthenticationSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    @pre_dump
    def _verify_dump(self, data, **kwargs):
        # Declare required attributes
        self.dump_fields.update(
            headers = fields.Nested(HeadersSchema, attribute='headers', required=True),
            devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices', required=True))
        )
        # Verify Authentication non-required attribute.
        if data.authentication:
            self.dump_fields.update(
                authentication = fields.Nested(AuthenticationSchema, attribute='authentication')
            )
        return data
