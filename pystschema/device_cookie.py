import hashlib
from datetime import datetime
from marshmallow import Schema, fields

class DeviceCookie:
    """The DeviceCookie is an utility
    class used for the DeviceClass to
    handle encrypted updates over the
    device.

        :::param cookie"""
    def __init__(self, cookie: str):
        self.cookie = cookie

    @classmethod
    def issue(cls):
        """Return a DeviceCookie instance with
        datetime.now() encrypted using md5 algorithm."""
        timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        cookie_hash = hashlib.md5(timestamp.encode()).hexdigest()
        return cls(cookie=cookie_hash)


class DeviceCookieSchema(Schema):
    """The DeviceCookieSchema handles the
    serialization of the DeviceCookie class."""
    cookie = fields.Str()


