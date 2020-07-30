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

    def __init__(self, devices: list, request_id: str) -> 'DiscoveryResponse':
        BaseResponse.__init__(self, interaction_type='discoveryResponse', request_id=request_id)
        self.devices = devices


class DiscoveryResponseSchema(Schema):  # Refactor Schema as StateRefreshResponseSchema
    """
    The DiscoveryResponseSchema handles
    the serialization of the DiscoveryResponse
    class supporting the nested
    DeviceDiscoverySchema and HeadersSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices'))
    headers = fields.Nested(HeadersSchema, attribute='headers')

    @pre_dump
    def _dump_authentication(self, data, **kwargs):
        if data.headers:
            self.dump_fields.update(
                headers = fields.Nested(HeadersSchema, attribute='headers'),
                devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices'))
            )
        if data.authentication:
            self.dump_fields.update(
                authentication = fields.Nested(AuthenticationSchema, attribute='authentication')
            )
        return data