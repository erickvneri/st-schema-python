"""
The Device interface provides a series of
methods to collect the information about
the devices that will be served to the
SmartThings Schema Connector integration
type.
"""
from stschema.util.base_modules import (
    BaseDevice,
    DeviceContext,
    ManufacturerInfo,
    BaseState,
    BaseError,
    BaseCookie,
    StateErrorEnum
)


class SchemaDevice(BaseDevice):
    """
    The Device interface inherits its
    attributes from the BaseDevice class.
        :::param external_device_id (required)
        :::param friendly_name (required)
        :::param device_handler_type (required)
        :::param device_unique_id
        :::param device_cookie
    """

    def __init__(self,
                 external_device_id=None,
                 friendly_name=None,
                 device_handler_type=None,
                 device_unique_id=None,
                 device_cookie=None) -> 'SchemaDevice':
        BaseDevice.__init__(self,
                            external_device_id,
                            friendly_name,
                            device_unique_id,
                            BaseCookie(device_cookie),
                            device_handler_type)

        self.states = []
        self.device_error = None
        self.device_context = None
        self.manufacturer_info = None

    # def set_mn(self, *args_info, **kwargs_info):
    def set_mn(self, manufacturer_name, model_name, hw_version, sw_version):
        """Defines the device's manufacturer information.
        Returns an instance of the ManufacturerInfo class.
            :::param manufacturer_name (required)
            :::param model_name (required)
            :::param hw_version
            :::param sw_version"""
        self.manufacturer_info = ManufacturerInfo(
            manufacturer_name,
            model_name,
            hw_version,
            sw_version
        )

    def set_context(self, room_name, groups, categories):
        """Defines the device's context information.
        Returns an instance of the DeviceContext class.
            :::param room_name
            :::param groups
            :::param categories"""
        # Type handling for list arguments
        if not isinstance(groups, list):
            raise TypeError('"groups" must be list instance, not (%s, %s)' % (type(groups), groups))
        elif not isinstance(categories, list):
            raise TypeError('"categories" must be list instance, not (%s, %s)' % (type(categories), categories))

        self.device_context = DeviceContext(room_name,
                                            groups,
                                            categories)

    # def set_state(self, *args_info, **kwargs_info):
    def set_state(self, capability, attribute, value, unit=None, component='main'):
        """Defines the device's state by
        adding one capability-state per call.
        Returns an instance of the BaseState class."""
        new_state = BaseState(capability=capability,
                              attribute=attribute,
                              value=value,
                              unit=unit,
                              component=component)
        self.states.append(new_state)

    def set_error_state(self, error_enum: str='DEVICE-UNAVAILABLE', detail: str='unexpected error occurred.'):
        """
        Defines the error state of the device.
        Supported device error enumerators:
            - DEVICE-UNAVAILABLE
            - CAPABILITY-NOT-SUPPORTED
            - RESOURCE-CONSTRAINT-VIOLATION
            - DEVICE-DELETED

            :::param error_enum: "DEVICE-UNAVAILABLE" by default.
            :::param detail: detail or message about device error
        """

        try:
            error_enum = StateErrorEnum(error_enum)
        except ValueError as e:
            raise ValueError('Device error enumerator not supported: %s' % error_enum)
        else:
            # self._set_error_state(error_enum.value, detail)
            err = BaseError(error_enum=error_enum.value, detail=detail)
            self.device_error = [err]
