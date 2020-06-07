from marshmallow import Schema, fields
from stschema.base.util import HeadersSchema
from stschema.interface.schemas import DeviceErrorSchema


class DeviceErrorResponseSchema(Schema):
    """The DeviceErrorResponse handles
    the serialization of the StateResponse
    class. Used in case there's a device
    error enum at the Device instance
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions."""

    headers = fields.Nested(HeadersSchema, attribute='headers')
    deviceState = fields.List(fields.Nested(DeviceErrorSchema), attribute='device_state')
