from marshmallow import Schema, fields
from stschema.util import (
    CookieSchema,
    ManufacturerSchema,
    DeviceContextSchema
)


class DeviceDiscoverySchema(Schema):
    """The DeviceDiscoverySchema handles
    the serialization of the SchemaDevice
    class supporting the nested
    CookieSchema, ManufacturerSchema, and
    DeviceContextSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects."""

    externalDeviceId = fields.Field(attribute='external_device_id')
    friendlyName = fields.Field(attribute='friendly_name')
    deviceHandlerType = fields.Field(attribute='device_handler_type')
    deviceUniqueId = fields.Field(attribute='device_unique_id')
    deviceCookie = fields.Nested(CookieSchema, attribute='device_cookie')
    manufacturerInfo = fields.Nested(ManufacturerSchema, attribute='manufacturer_info')
    deviceContext = fields.Nested(DeviceContextSchema, attribute='device_context')
