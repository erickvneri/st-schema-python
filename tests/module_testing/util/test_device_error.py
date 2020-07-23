import pytest
from stschema.util import StateErrorEnum, DeviceError


class TestBaseDeviceError(object):
    def test_class_documentation(self):
        assert DeviceError
        assert DeviceError.__doc__
        assert len(DeviceError.__doc__)

    def test_error_instance(self):
        result = DeviceError(error_enum='DEVICE-UNAVAILABLE', detail='device out of range')
        assert isinstance(result, DeviceError)
        assert result.error_enum
        assert result.detail

    def test_type_error(self):
        with pytest.raises(TypeError):
            result = DeviceError()