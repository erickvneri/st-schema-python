import pytest
from stschema.base.device import ManufacturerInfo
from stschema import Device


class TestDeviceInstanciation:
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
