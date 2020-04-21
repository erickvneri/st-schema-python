from marshmallow import Schema, fields

class BaseDeviceCookie:
    """The DeviceCookie is an utility
    class used for the DeviceClass to
    handle encrypted updates over the
    device.
        :::param cookie"""

    def __init__(self, **kwargs):
        self.cookie = kwargs


class DeviceCookieSchema(Schema):
    """The DeviceCookieSchema handles the
    serialization of the DeviceCookie class.
        e.g.:
        {'cookie': {'update': '2020-04-21'}}"""

    cookie = fields.Field(attribute='cookie')


