# The Device interface provides a series of
# methods to collect the information about
# the devices that will be served to the
# SmartThings Schema Connector integration
# type.
from stschema.base.util import BaseCookie, StateErrorEnum
from stschema.base.device import (BaseDevice, DeviceContext,
                                  ManufacturerInfo, BaseState, DeviceError)


class Device(BaseDevice):
    """The Device interface inherits its
    attributes from the BaseDevice class.
        :::param external_device_id (required)
        :::param friendly_name (required)
        :::param device_handler_type (required)
        :::param device_unique_id
        :::param device_cookie"""

    def __init__(self, *args_info, **kwargs_info):
        # By default instance is being created
        # from kwargs_info to discard None values.
        BaseDevice.__init__(
            self,
            external_device_id=kwargs_info.get('external_device_id'),
            friendly_name=kwargs_info.get('friendly_name'),
            device_unique_id=kwargs_info.get('device_unique_id'),
            device_cookie=BaseCookie(kwargs_info.get('device_cookie')),
            device_handler_type=kwargs_info.get('device_handler_type')
        )
        # Args instance handler
        if args_info:
            self._device_arg_instance(args_info)

        self.states = []
        self.device_error = None
        self.device_context = None
        self.manufacturer_info = None

    def _device_arg_instance(self, args_info):
        # Handler to define Device instance
        # from straight args.
        for i in range(len(args_info)):
            if len(args_info) > 5:
                unexpected_args = [arg for arg in args_info[5:]]
                raise TypeError('Unexpected arguments: %s' % unexpected_args)
            if i == 0:
                self.external_device_id = args_info[0]
            if i == 1:
                self.friendly_name = args_info[1]
            if i == 2:
                self.device_handler_type = args_info[2]
            if i == 3:
                self.device_unique_id = args_info[3]
            if i == 4:
                self.device_cookie = BaseCookie(args_info[4])

    def set_mn(self, *args_info, **kwargs_info):
        """Defines the device's manufacturer information.
        Returns an instance of the ManufacturerInfo class.
            :::param manufacturer_name (required)
            :::param model_name (required)
            :::param hw_version
            :::param sw_version"""
        # By default Manufacturer information is being
        # declared from kwargs_info.
        manufacturer_name = kwargs_info.get('manufacturer_name')
        model_name = kwargs_info.get('model_name')
        hw_version = kwargs_info.get('hw_version')
        sw_version = kwargs_info.get('sw_version')

        # Iteration to check if Manufacturer's information
        # has been passed with straight arguments and if
        # key word arguemts haven't been defined already.
        for i in range(len(args_info)):
            if len(args_info) > 4:
                unexpected_arguments = [arg for arg in args_info[4:]]
                raise TypeError('Unexpected arguments: %s' % unexpected_arguments)
            elif i == 0 and manufacturer_name is None:
                manufacturer_name = args_info[0]
            elif i == 1 and not model_name:
                model_name = args_info[1]
            elif i == 2 and not hw_version:
                hw_version = args_info[2]
            elif i == 3 and not sw_version:
                sw_version = args_info[3]

        self._set_mn(
            manufacturer_name,
            model_name,
            hw_version,
            sw_version
        )

    def _set_mn(self, manufacturer_name, model_name, hw_version, sw_version):
        # Private method called to instance
        # ManufacturerInfo class after data
        # has been prepared by public method.
        self.manufacturer_info = ManufacturerInfo(
            manufacturer_name,
            model_name,
            hw_version,
            sw_version
        )

    def set_context(self, *args_info, **kwargs_info):
        """Defines the device's context information.
        Returns an instance of the DeviceContext class.
            :::param room_name
            :::param groups
            :::param categories"""
        # By  default DeviceContext information is being
        # declared from kwargs_info.
        room_name = kwargs_info.get('room_name')
        groups = kwargs_info.get('groups')
        categories = kwargs_info.get('categories')

        # Handle redefinition of device_context
        # based on straight arguments.
        for i in range(len(args_info)):
            if len(args_info) > 3:
                unexpected_arguments = [arg for arg in args_info[3:]]
                raise TypeError('Unexpected arguments: %s' % unexpected_arguments)
            elif i == 0 and not room_name:
                room_name = args_info[0]
            elif i == 1 and not groups:
                groups = args_info[1]
            elif i == 2 and not categories:
                categories = args_info[2]

        # Type handling for list arguments
        if not isinstance(groups, list):
            raise TypeError('list argument expected, not (%s, %s)' % (type(groups), groups))
        elif not isinstance(categories, list):
            raise TypeError('list argument expected, not (%s, %s)' % (type(categories), categories))

        self._set_context(
            room_name,
            groups,
            categories
        )

    def _set_context(self, room_name, groups, categories):
        # Private method called to instanciate
        # the DeviceContext class after data has
        # been prepared by public method.
        self.device_context = DeviceContext(
            room_name,
            groups,
            categories
        )

    def set_state(self, *args_info, **kwargs_info):
        """Defines the device's state by
        adding one capability-state per call.
        Returns an instance of the BaseState class."""
        # By default State information is
        # being declared from kwargs_info.
        component = kwargs_info.get('component')
        capability = kwargs_info.get('capability')
        attribute = kwargs_info.get('attribute')
        value = kwargs_info.get('value')
        unit = kwargs_info.get('unit')

        # Iteration to check if State's information
        # has been passed with straight arguments and if
        # key word arguemts haven't been defined already.
        for i in range(len(args_info)):
            if len(args_info) > 5:
                unexpected_arguments = [arg for arg in args_info[5:]]
                raise TypeError('Unexpected arguments: %s' % unexpected_arguments)
            if i == 0 and not capability:
                capability = args_info[0]
            elif i == 1 and not attribute:
                attribute = args_info[1]
            elif i == 2 and not value:
                value  = args_info[2]
            elif i == 3 and not unit:
                unit = args_info[3]
            elif i == 4 and not component:
                component = args_info[4]

        self._set_state(
            capability,
            attribute,
            value,
            unit,
            component
        )

    def _set_state(self, capability, attribute, value, unit, component):
        # Private method called to instanciate
        # the BaseState class after data has
        # been prepared by public method.
        if not component:
            component = 'main'
        new_state = BaseState(
            capability=capability,
            attribute=attribute,
            value=value,
            unit=unit,
            component=component
        )
        self.states.append(new_state)

    def set_error_state(self, error_enum: str='DEVICE-UNAVAILABLE', detail: str='unexpected error occurred.'):
        """Defines the error state of the device.
        Supported device error enumerators:
            - DEVICE-UNAVAILABLE
            - CAPABILITY-NOT-SUPPORTED
            - RESOURCE-CONSTRAINT-VIOLATION
            - DEVICE-DELETED

            :::param error_enum: (DEVICE-UNAVAILABLE by default).
            :::param detail: detail or message about device error"""

        try:
            error_enum = StateErrorEnum(error_enum)
        except ValueError as e:
            raise ValueError('Device error enumerator not supported: %s' % error_enum)
        else:
            self._set_error_state(
                error_enum.value,
                detail
            )

    def _set_error_state(self, error_enum, detail):
        # Private method that will define
        # the DeviceError state device's
        # attribute.
        err = DeviceError(
            error_enum=error_enum,
            detail=detail
        )
        self.device_error = [err]
