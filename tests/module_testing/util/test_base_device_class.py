import pytest
from stschema.util import BaseDevice


class TestBaseDevice(object):
    """TestBaseDevice class defined to test the
    BaseDevice class. This class will extend to
    its further device implementation."""

    @pytest.fixture
    def device_instance(self):
        device_instance = BaseDevice(
            external_device_id=__name__,
            device_cookie=__name__,
            friendly_name=__name__,
            device_handler_type=__name__,
            device_unique_id=__name__
        )
        yield device_instance

    def test_class_documentation(self):
        assert BaseDevice.__doc__
        assert len(BaseDevice.__doc__) != 0

    def test_base_device_instance(self, device_instance):
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

    def test_type_error_wrong_attrs(self):
        with pytest.raises(TypeError):
            BaseDevice(protocol=__name__)
            BaseDevice(secret=__name__)
            BaseDevice(key=__name__)

    def test_type_error_extra_value(self):
        with pytest.raises(TypeError):
            BaseDevice(
                external_device_id=__name__,
                device_cookie=__name__,
                friendly_name=__name__,
                device_handler_type=__name__,
                device_unique_id=__name__,
                key=__name__
            )