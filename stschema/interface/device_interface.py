# The Device interface provides a series of
# methods to collect the information about
# the devices that will be served to the
# SmartThings Schema Connector integration
# type.
from stschema.base.util import BaseCookie, ErrorEnum
from stschema.base.device import (BaseDevice, DeviceContext,
                                  ManufacturerInfo, BaseState, DeviceError)


class Device(BaseDevice):
    """The Device interface inherits its
    attributes from the BaseDevice class.
        :::param external_device_id (required)
        :::param friendly_name (required)
        :::param device_unique_id (required)
        :::param device_cookie (None by default)
        :::param device_handler_type (required)"""

    def __init__(self, **info):
        BaseDevice.__init__(self,
            external_device_id=info.get('external_device_id'),
            friendly_name=info.get('friendly_name'),
            device_unique_id=info.get('device_unique_id'),
            device_cookie=BaseCookie(info.get('device_cookie')),
            device_handler_type=info.get('device_handler_type'))
        self.states = []
        self.device_error = []
        self.device_context = None
        self.manufacturer_info = None

    def set_context(self, **context):
        """Defines the device's context information.
        Returns an instance of the DeviceContext class.
            :::param room_name
            :::param groups
            :::param categories"""

        self.device_context = DeviceContext(
            room_name=context.get('room_name'),
            groups=context.get('groups'),
            categories=context.get('categories'))

    def set_mn(self, **info):
        """Defines the device's manufacturer information.
        Returns an instance of the ManufacturerInfo class.
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

    def set_state(self, capability: str, attribute: str, value: str or int, component: str = 'main', unit: str = None):
        """Defines the device's state by
        adding one capability-state per call.
        Returns an instance of the BaseState class."""

        new_state = BaseState(
            component=component,
            capability=f'st.{capability}',
            attribute=attribute,
            value=value,
            unit=unit
        )
        self.states.append(new_state)

    def set_error_state(self, error_enum: ErrorEnum = 'DEVICE-UNAVAILABLE', detail: str = None):
        """Defines the error specification when
        a the device's API detectes an error.
        Returns an instance of the DeviceError
        class.
            :::param error_enum: based on the
            documented errorEnum values."""

        err = DeviceError(error_enum=error_enum, detail=detail)
        self.device_error.append(err)
