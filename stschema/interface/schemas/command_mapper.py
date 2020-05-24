from marshmallow import Schema, fields


class DeviceCommandMapper(Schema):
    """The DeviceCommandMapper will extract
    the relevant device's data from the
    Command Request."""

    def __init__(self):
        Schema.__init__(self, unknown=True)

    externalDeviceId = fields.Str(attribute='external_device_id')
    commands = fields.Field()
