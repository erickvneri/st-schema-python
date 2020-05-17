from marshmallow import Schema, fields
from stschema.base.util import DeviceCookieSchema


class DeviceCommandMapper(Schema):
    """The DeviceCommandMapper schema will
    parse the Request payload into snake-case
    format to directly handle values with the
    Device Interface"""
    def __init__(self):
        Schema.__init__(self, unknown=True)

    externalDeviceId = fields.Str(attribute='external_device_id')
    commands = fields.Field()
