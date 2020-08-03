from marshmallow import Schema, fields
from stschema.util.base_modules import CookieSchema, StateSchema


class DeviceStateSchema(Schema):
    """
    The DeviceStateSchema handles the
    serialization of the SchemaDevice
    class supporting the nested
    CookieSchema and StateSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceCookie = fields.Nested(CookieSchema, attribute='device_cookie')
    states = fields.List(fields.Nested(StateSchema), attribute='states')
