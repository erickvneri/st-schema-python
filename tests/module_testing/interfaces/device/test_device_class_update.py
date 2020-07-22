import pytest
from stschema.base.device import ManufacturerInfo
from stschema import Device


class TestDeviceInstanciation:
    def test_device_instance_from_args(self):
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
        # Device default definitions
        # using straight arguments and
        # passing unexpected arguments.
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