from marshmallow import Schema, fields
from stschema.base.device import StateSchema
from stschema.base.util import DeviceCookieSchema


class DeviceStateSchema(Schema):
    """The DeviceStateSchema class handles the
    serialization of the Device State information
    accordingly to the ST Schema/StateRefreshResponse
    documentation.

    It parses the Snake Cased attributes to a
    Camel Case format following REST conventions
    for Cloud-to-Cloud communication:
        :::param external_device_id -> externalDeviceId
        :::param device_cookie -> deviceCookie"""

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceCookie = fields.Nested(DeviceCookieSchema, attribute='device_cookie')
    states = fields.List(fields.Nested(StateSchema), attribute='states')
