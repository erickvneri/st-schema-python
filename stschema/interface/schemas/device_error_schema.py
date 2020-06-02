from stschema.base.device import BaseErrorSchema
from stschema.base.util import DeviceCookieSchema
from marshmallow import Schema, fields


class DeviceErrorSchema(Schema):
    """The DeviceErrorSchema handles the
    serialization of the Device instance
    with an error assigned.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions.
        :::param external_device_id -> externalDeviceId
        :::param device_cookie -> deviceCookie
        :::param device_error -> deviceError"""

    externalDeviceId = fields.Str(attribute='external_device_id')
    deviceError = fields.List(fields.Nested(BaseErrorSchema), attribute='device_error')
