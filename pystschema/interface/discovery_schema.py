from marshmallow import Schema, fields
from pystschema.base import ManufacturerSchema, DeviceContextSchema, DeviceCookieSchema

class DiscoveryDeviceSchema(Schema):
    """The DiscoverySchema returns the formal
    representation of a device in a Discovery
    Response.

    It handles the keys for Nested schemas:
        - DeviceSchema
        - DeviceCookieSchema
        - ManufacturerSchema
        - DeviceContextSchema
        """
    externalDeviceId = fields.Field(attribute='external_device_id', dump_only=True)
    friendlyName = fields.Field(attribute='friendly_name', dump_only=True)
    deviceHandlerType = fields.Field(attribute='device_handler_type', dump_only=True)
    deviceUniqueId = fields.Field(attribute='device_unique_id', dump_only=True)
    deviceCookie = fields.Nested(DeviceCookieSchema, attribute='device_cookie')
    manufacturerInfo = fields.Nested(ManufacturerSchema, attribute='manufacturer_info')
    deviceContext = fields.Nested(DeviceContextSchema, attribute='device_context')