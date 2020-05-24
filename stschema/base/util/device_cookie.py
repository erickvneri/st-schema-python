from marshmallow import Schema, fields


class BaseCookie:
    """The DeviceCookie class handles
    the device's cookie value.
        :::param cookie"""

    def __init__(self, cookie: str):
        self.cookie = cookie


class DeviceCookieSchema(Schema):
    """The DeviceCookieSchema handles the
    serialization of the DeviceCookie class."""

    cookie = fields.Str(attribute='cookie')


