from marshmallow import Schema, fields

class BaseCookie:
    """The DeviceCookie is an utility
    class used for the DeviceClass to
    handle encrypted updates over the
    device.
        :::param cookie"""

    def __init__(self, cookie: str):
        self.cookie = cookie

class DeviceCookieSchema(Schema):
    """The DeviceCookieSchema handles the
    serialization of the DeviceCookie class.
        e.g.:
        {'cookie': f'{value}'}"""

    cookie = fields.Str(attribute='cookie')


