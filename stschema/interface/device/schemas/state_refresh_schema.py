from marshmallow import Schema, fields
from stschema.base.device import StateSchema
from stschema.base.util import DeviceCookieSchema


class DeviceStateSchema(Schema):
    """The DeviceStateSchema handles the
    serialization of the device's state information.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions.
        :::param external_device_id -> externalDeviceId
        :::param device_cookie -> deviceCookie"""

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceCookie = fields.Nested(DeviceCookieSchema, attribute='device_cookie')
    states = fields.List(fields.Nested(StateSchema), attribute='states')
