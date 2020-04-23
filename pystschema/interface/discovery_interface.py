from pystschema.base import BaseDevice, BaseDeviceContext, BaseDeviceCookie, BaseManufacturer

class DeviceInterface(BaseDevice):
    """Inherits from BaseDevice.

        :::param external_device_id: required values
        :::param friendly_name: required values
        :::param device_handler_type: required values
        :::param device_cookie: default as None
        :::param device_unique_id: required value

        Extends by adding the next methods:
            - set_context
            - set_mn
            - set_cookie"""

    def __init__(
            self, external_device_id: str, friendly_name: str, device_unique_id: str, device_cookie: object, device_handler_type: str
                 ):
        BaseDevice.__init__(
            self, external_device_id, friendly_name, device_unique_id, device_cookie, device_handler_type
        )
        self.device_context = None
        self.manufacturer_info = None

    def set_context(self, room_name: str, groups: list, categories: list):
        """Defines the device_context values accordingly to the ST Schema specifications.

            :::param room_name
            :::param groups
            :::param categories"""

        self.device_context = BaseDeviceContext(
            room_name=room_name, groups=groups, categories=categories
        )

    def set_mn(self, manufacturer_name: str, model_name: str, hw_version: str, sw_version: str):
        """Defines the manufacturer_info  values accordingly to the ST Schema specifications.

            :::param manufacturer_name
            :::param model_name
            :::param hw_version
            :::param sw_version
        """

        self.manufacturer_info = BaseManufacturer(
            manufacturer_name=manufacturer_name, model_name=model_name, hw_version=hw_version, sw_version=sw_version
        )

    def set_cookie(self, cookie: str):
        """Defines the device cookie"""

        self.device_cookie = BaseDeviceCookie(cookie=cookie)
