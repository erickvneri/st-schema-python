from marshmallow import Schema, fields
from stschema.util.base_modules import (CookieSchema,
                                        ManufacturerSchema,
                                        DeviceContextSchema)


class DeviceDiscoverySchema(Schema):
    """
    The DeviceDiscoverySchema handles
    the serialization of the SchemaDevice
    class supporting the nested
    CookieSchema, ManufacturerSchema, and
    DeviceContextSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    externalDeviceId = fields.Field(attribute='external_device_id', required=True)
    friendlyName = fields.Field(attribute='friendly_name', required=True)
    deviceHandlerType = fields.Field(attribute='device_handler_type', required=True)
    deviceUniqueId = fields.Field(attribute='device_unique_id')
    deviceCookie = fields.Nested(CookieSchema, attribute='device_cookie')
    manufacturerInfo = fields.Nested(ManufacturerSchema, attribute='manufacturer_info', required=True)
    deviceContext = fields.Nested(DeviceContextSchema, attribute='device_context')
