from stschema.base.device_cookie import BaseCookie


class BaseDevice:
    """The BaseDevice class is the basic SmartThings
    Device representation that will contain the main
    attributes for identifying a Cloud Integrated
    device:
        :::param external_device_id: device id for a
        third-party cloud.
        :::param friendly_name: Name set by the user.
        :::param device_handler_type: value referred
        at the main ST-Schema documentation:
        https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/device-handler-types.html
        :::param device_cookie: DeviceCookie object.
        :::param unique_device_id"""

    def __init__(
        self, external_device_id: str, friendly_name: str, device_unique_id: str,
        device_cookie: str, device_handler_type: str
    ):
        self.external_device_id = external_device_id
        self.friendly_name = friendly_name
        self.device_unique_id = device_unique_id
        self.device_cookie = BaseCookie(device_cookie)
        self.device_handler_type = device_handler_type
