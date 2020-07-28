from marshmallow import Schema, fields
from stschema.util import BaseErrorSchema


class DeviceErrorSchema(Schema):
    """
    The DeviceErrorSchema handles the
    serialization of the SchemaDevice
    class supporting the nested
    BaseErrorSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceError = fields.List(fields.Nested(BaseErrorSchema), attribute='device_error')
