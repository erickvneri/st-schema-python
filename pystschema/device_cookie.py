import hashlib
from datetime import datetime
from marshmallow import Schema, fields

class DeviceCookie:
    """The DeviceCookie for creating cookies
        over the device.

        Methods defined here:

        issue(cls) -> return a cookie with
                        datetime.now() hashed."""

    def __init__(self, cookie):
        self.cookie = cookie

    @classmethod
    def issue(cls):
        timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        cookie_hash = hashlib.md5(timestamp.encode()).hexdigest()
        return cls(cookie=cookie_hash)


class DeviceCookieSchema(Schema):
    cookie = fields.Str()


