from marshmallow import Schema, fields
from stschema.util import (
    DeviceCookieSchema,
    ManufacturerSchema,
    DeviceContextSchema
)


class DeviceDiscoverySchema(Schema):
    """The DeviceDiscoverySchema handles the
    serialization of the Device interface."""

    externalDeviceId = fields.Field(attribute='external_device_id')
    friendlyName = fields.Field(attribute='friendly_name')
    deviceHandlerType = fields.Field(attribute='device_handler_type')
    deviceUniqueId = fields.Field(attribute='device_unique_id')
    deviceCookie = fields.Nested(DeviceCookieSchema, attribute='device_cookie')
    manufacturerInfo = fields.Nested(ManufacturerSchema, attribute='manufacturer_info')
    deviceContext = fields.Nested(DeviceContextSchema, attribute='device_context')
