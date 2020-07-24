from marshmallow import Schema, fields


class BaseCookie:
    """The BaseCookie represents the
    a customizable cookie to control
    updates metadata on devices.
        :::param cookie"""

    def __init__(self, cookie) -> 'BaseCookie':
        self.cookie = cookie


class CookieSchema(Schema):
    """The CookieSchema handles the
    serialization of the BaseCookie
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects."""

    cookie = fields.Field(attribute='cookie')
