from marshmallow import Schema, fields

class BaseDevice:
    """The BaseDevice class is the basic SmartThings
    Device representation that will contain the main
    identification attributes of a Cloud-to-Cloud
    device:
        :::param external_device_id: device id for a
        third-party cloud.
        :::param friendly_name: Name set by the user.
        :::param device_handler_type: value referred
        at the main ST-Schema documentation:
        https://smartthings.developer.samsung.com/docs//devices/smartthings-schema/device-handler-types.html
        :::param device_cookie: DeviceCookie object."""
    def __init__(
        self, external_device_id: str, device_cookie: object, friendly_name: str, device_handler_type: str
    ):
        self.external_device_id = external_device_id
        self.device_cookie = device_cookie or dict()
        self.friendly_name = friendly_name
        self.device_handler_type = device_handler_type


class DeviceSchema(Schema):
    """The DeviceSchema class will handle the
    serialization of the BaseDevice and Device
    classes. It parses the snake cased attributes
    to Camel Case attributes as the ST-Schema
    documentation refers:

        :::param external_device_id -> externalDeviceId
        :::param friendly_name -> friendlyName
        :::param device_handler_type -> deviceHandlerType
        :::param device_cookie -> deviceCookie"""
    externalDeviceId = fields.Field(attribute='external_device_id')
    deviceCookie = fields.Field(attribute='device_cookie')
    friendlyName = fields.Field(attribute='friendly_name')
    deviceHandlerType = fields.Field(attribute='device_handler_type')

