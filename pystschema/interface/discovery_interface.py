from pystschema.base import BaseDevice, DeviceContext, ManufacturerInfo

class DeviceInterface(BaseDevice):
    """Inherits from BaseDevice.

        :::param external_device_id: required values
        :::param friendly_name: required values
        :::param device_handler_type: required values
        :::param device_cookie: default as None
        :::param device_unique_id: required value

        Extends by adding the next methods:
            - set_context
            - set_mn"""

    def __init__(self, **info):
        BaseDevice.__init__(self,
                            external_device_id=info.get('external_device_id'),
                            friendly_name=info.get('friendly_name'),
                            device_unique_id=info.get('device_unique_id'),
                            device_cookie=info.get('device_cookie'),
                            device_handler_type=info.get('device_handler_type')
                            )
        self.device_context = None
        self.manufacturer_info = None

    def set_context(self, **context):
        """Defines the device_context values accordingly to the ST Schema specifications.

            :::param room_name
            :::param groups
            :::param categories"""

        self.device_context = DeviceContext(
            room_name=context.get('room_name'),
            groups=context.get('groups'),
            categories=context.get('categories')
        )

    def set_mn(self, **info):
        """Defines the manufacturer_info  values accordingly to the ST Schema specifications.

            :::param manufacturer_name
            :::param model_name
            :::param hw_version
            :::param sw_version"""

        self.manufacturer_info = ManufacturerInfo(
            manufacturer_name=info.get('manufacturer_name'),
            model_name=info.get('model_name'),
            hw_version=info.get('hw_version'),
            sw_version=info.get('sw_version')
        )

