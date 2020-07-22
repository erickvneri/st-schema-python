# Test suite over functionalities that
# the Device class interface provices.
#
# A features that is being tested
# is the flexibility of a Device
# instantiation, supporting for
# straight (*args) and key word
# (**kwargs) arguments.
#
# Some Test-to-Fail test cases habe
# been included. These Exceptions help
# develoeprs to improve creation of
# Device instances.
import pytest
from stschema.base.device import ManufacturerInfo
from stschema import Device


class TestDeviceInterface:
    """Test Suite on Device class interface"""
    class TestDeviceClassElements:
        # Test case on the construction
        # of the Device class interface.
        def test_documentation(self):
            # Class documentation
            assert Device.__doc__
            assert len(Device.__doc__) > 0

        def test_public_methods(self):
            # Public methods
            assert Device.set_context
            assert Device.set_mn
            assert Device.set_state
            assert Device.set_error_state

        def test_private_methods(self):
            # Private methods
            assert Device._set_context
            assert Device._set_mn
            assert Device._set_state
            assert Device._set_error_state
            assert Device._device_arg_instance


    class TestDeviceDefinition:
        # Test case on the initial Device
        # instance.
        def test_device_instance_from_args(self):
            # Base definition from
            # straight arguments (*args).
            device = Device(
                'external_device_id_arg',
                'friendly_name_arg',
                'device_handler_type_arg',
                'device_unique_id_arg',
                'device_cookie_arg'
            )
            assert device.external_device_id == 'external_device_id_arg'
            assert device.friendly_name == 'friendly_name_arg'
            assert device.device_handler_type == 'device_handler_type_arg'
            assert device.device_unique_id == 'device_unique_id_arg'
            assert device.device_cookie.cookie == 'device_cookie_arg'

        def test_device_instance_from_kwargs(self):
            # Base definition from
            # key word arguments (**kwargs)
            device = Device(
                external_device_id='external_device_id_kwarg',
                friendly_name='friendly_name_kwarg',
                device_handler_type='device_handler_type_kwarg',
                device_unique_id='device_unique_id_kwarg',
                device_cookie='device_cookie_kwarg'
            )
            assert device.external_device_id == 'external_device_id_kwarg'
            assert device.friendly_name == 'friendly_name_kwarg'
            assert device.device_handler_type == 'device_handler_type_kwarg'
            assert device.device_unique_id == 'device_unique_id_kwarg'
            assert device.device_cookie.cookie == 'device_cookie_kwarg'

        def test_type_error_unexpected_arg(self):
            # Test for unexpected arguments
            # when defining main instance
            # attributes.
            with pytest.raises(TypeError):
                Device(
                    'external_device_id_arg',
                    'friendly_name_arg',
                    'device_handler_type_arg',
                    'device_unique_id_arg',
                    'device_cookie_arg',
                    'UNEXPECTED_ARGUMENT_1',
                    'UNEXPECTED_ARGUMENT_2'
                )


    class TestManufacturerInfo:
        # Test case on the definition of the
        # device's manufacturer info attributes.
        def test_manufacturer_info_from_args(self):
            # Manufacturer Info default definition
            # using straight arguments. Checking order
            # and reliability of handler.
            device = Device()
            device.set_mn(
                'manufacturer_info_arg',
                'model_name_arg',
                'hardware_version_arg',
                'software_version_arg'
            )
            assert isinstance(device.manufacturer_info, ManufacturerInfo)
            assert device.manufacturer_info.manufacturer_name == 'manufacturer_info_arg'
            assert device.manufacturer_info.model_name == 'model_name_arg'
            assert device.manufacturer_info.hw_version == 'hardware_version_arg'
            assert device.manufacturer_info.sw_version == 'software_version_arg'

        def test_manufacturer_info_from_kwargs(self):
            # Manufacturer Info definition
            # from key word arguments (**kwargs).
            device = Device()
            device.set_mn(
                manufacturer_name='manufacturer_info_kwarg',
                model_name='model_name_kwarg',
                hw_version='hardware_version_kwarg',
                sw_version='software_version_kwarg'
            )
            assert isinstance(device.manufacturer_info, ManufacturerInfo)
            assert device.manufacturer_info.manufacturer_name == 'manufacturer_info_kwarg'
            assert device.manufacturer_info.model_name == 'model_name_kwarg'
            assert device.manufacturer_info.hw_version == 'hardware_version_kwarg'
            assert device.manufacturer_info.sw_version == 'software_version_kwarg'


        def test_type_error_unexpected_arguments(self):
            # Test for unexpected arguments
            # when defining Manufacturer's
            # Info attributes.
            with pytest.raises(TypeError):
                device = Device()
                device.set_mn(
                    'manufacturer_info_arg',
                    'model_name_arg',
                    'hardware_version_arg',
                    'software_version_arg',
                    'UNEXPECTED_ARGUMENT_1',
                    'UNEXPECTED_ARGUMENT_2'
                )


    class TestDeviceContext:
            # Test case on the definition of the
            # Device Context attributes for a Device
            # instance.
            def test_device_context_from_args(self):
                # Device Context default definition
                # using straight arguments. Checking order
                # and reliability of handler.
                device = Device()
                device.set_context(
                    'room_name_arg',
                    ['groups', 'list', 'args'],
                    ['categories', 'list', 'args']
                )
                assert device.device_context.room_name == 'room_name_arg'
                assert isinstance(device.device_context.groups, list)
                assert device.device_context.groups == ['groups', 'list', 'args']
                assert isinstance(device.device_context.categories, list)
                assert device.device_context.categories == ['categories', 'list', 'args']

            def test_device_context_from_kwargs(self):
                # Device Context definition from
                # key word arguments (**kwargs).
                device = Device()
                device.set_context(
                    room_name='room_name_kwarg',
                    groups=['groups', 'list', 'kwargs'],
                    categories=['categories', 'list', 'kwargs']
                )
                assert device.device_context.room_name == 'room_name_kwarg'
                assert isinstance(device.device_context.groups, list)
                assert device.device_context.groups == ['groups', 'list', 'kwargs']
                assert isinstance(device.device_context.categories, list)
                assert device.device_context.categories == ['categories', 'list', 'kwargs']

            def test_type_error_unexpected_arguments(self):
                # Test for unexpected arguments
                # when defining Device Context
                # attributes.
                with pytest.raises(TypeError):
                    device = Device()
                    device.set_context(
                        'room_name_arg',
                        ['groups', 'list', 'args'],
                        ['categories', 'list', 'args'],
                        'UNEXPECTED_ARGUMENT'
                    )

            def test_type_error_list_arg_expected(self):
                # Test for unexpected type if
                # args passed are not list.
                with pytest.raises(TypeError):
                    device = Device()
                    device.set_context(
                        'room_name_arg',
                        'groups_string_argument',
                        'categories_string_argument'
                    )


    class TestSetState:
        # Test Case on the definition of
        # states/capabilities as device's
        # state.
        def test_set_state_from_args(self):
            # State definition from straight
            # arguments.
            device = Device()
            device.set_state(
                'capability_arg',
                'attribute_arg',
                'value_arg',
                'unit_arg',
                'component_arg'
            )
            assert device.states[0].capability == 'capability_arg'
            assert device.states[0].attribute == 'attribute_arg'
            assert device.states[0].value == 'value_arg'
            assert device.states[0].unit == 'unit_arg'
            assert device.states[0].component == 'component_arg'

        def test_set_state_from_kwargs(self):
            # State/Capability definition from
            # kwy word arguments (**kwargs).
            device = Device()
            device.set_state(
                capability='capability_kwarg',
                attribute='attribute_kwarg',
                value='value_kwarg',
                unit='unit_kwarg',
                component='component_kwarg'
            )
            assert device.states[0].capability == 'capability_kwarg'
            assert device.states[0].attribute == 'attribute_kwarg'
            assert device.states[0].value == 'value_kwarg'
            assert device.states[0].unit == 'unit_kwarg'
            assert device.states[0].component == 'component_kwarg'

        def test_type_error_set_state_unexpected_arguments(self):
            # Test for unexpected arguments
            # when defining State/Capability
            # attributes.
            with pytest.raises(TypeError):
                device = Device()
                device.set_state(
                    'capability_arg',
                    'attribute_arg',
                    'value_arg',
                    'unit_arg',
                    'component_arg',
                    'UNEXPECTED_ARGUMENT'
                )


    class TestDeviceError:
        # Test Case on DeviceError states. .
        def test_error_state_default_definition(self):
            # Default Device Error state definition.
            device = Device()
            device.set_error_state()
            assert device.device_error[0].error_enum == 'DEVICE-UNAVAILABLE'
            assert device.device_error[0].detail == 'unexpected error occurred.'

        def test_error_state_from_args(self):
            # Device Error state definition
            # from straight arguments (*args).
            device = Device()
            device.set_error_state('CAPABILITY-NOT-SUPPORTED', 'detail_arg')
            assert device.device_error[0].error_enum == 'CAPABILITY-NOT-SUPPORTED'
            assert device.device_error[0].detail == 'detail_arg'

        def test_error_state_from_kwargs(self):
            # Device Error state definition
            # from key word arguments (**kwargs).
            device = Device()
            device.set_error_state(error_enum='CAPABILITY-NOT-SUPPORTED', detail='detail_kwarg')
            assert device.device_error[0].error_enum == 'CAPABILITY-NOT-SUPPORTED'
            assert device.device_error[0].detail == 'detail_kwarg'

        def test_type_error_enum_not_supported(self):
            # Device Error Exception for
            # non-suppoted error enumerators.
            with pytest.raises(ValueError):
                device = Device()
                device.set_error_state('ERROR-ENUM-NOT-SUPPORTED')
