from marshmallow import Schema, fields
from stschema.base.util import DeviceCookieSchema


class DeviceCommandMapper(Schema):
    """The DeviceCommandMapper will extract
    the relevant device's data from the
    Command Request."""

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceCookie = fields.Nested(DeviceCookieSchema, attribute='device_cookie')
    commands = fields.List(fields.Field())
