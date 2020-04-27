import pytest
from stschema.base import BaseDevice

class TestBaseDevice:
    """TestBaseDevice class defined to test the
    BaseDevice class. This class will extend to
    its further device implementation."""

    @pytest.fixture
    def device_instance(self):
        device_instance = BaseDevice(
            external_device_id='devx-122-jaku',
            device_cookie='test_cookie',
            friendly_name='testo',
            device_handler_type='c2c-test-handler',
            device_unique_id='123abc'
        )
        yield device_instance

    def test_class_construction(self):
        assert BaseDevice.__doc__
        assert len(BaseDevice.__doc__) != 0

    def test_device_definition(self, device_instance):
        """This test will verify the main functionality
        of  the BaseDevice class."""
        assert isinstance(device_instance, BaseDevice)
        assert device_instance.external_device_id
        assert device_instance.device_cookie
        assert device_instance.friendly_name
        assert device_instance.device_handler_type
        assert device_instance.device_unique_id

    def test_type_error_definition(self):
        with pytest.raises(TypeError):
            device_instance = BaseDevice()
            device_instance.external_device_id = 'devx-122-jaku'
            device_instance.device_cookie = 'test_cookie'
            device_instance.friendly_name = 'testo'
            device_instance.device_handler_type = 'c2c-test-handler'
            device_instance.device_unique_id = '123abc'
            assert device_instance.external_device_id
            assert device_instance.device_cookie is not None
            assert device_instance.friendly_name
            assert device_instance.device_handler_type
            assert device_instance.device_unique_id
