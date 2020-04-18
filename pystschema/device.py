from marshmallow import Schema, fields
from pystschema.device_cookie import DeviceCookieSchema

class Device:
    def __init__(self, external_device_id: str, device_cookie: dict, friendly_name: str, device_handler_type: str):
        self.external_device_id = external_device_id
        self.device_cookie = device_cookie or dict()
        self.friendly_name = friendly_name
        self.device_handler_type = device_handler_type

class DeviceSchema(Schema):
    external_device_id = fields.Str()
    device_cookie = fields.Nested(DeviceCookieSchema)
    friendly_name = fields.Str()
    device_handler_type = fields.Str()