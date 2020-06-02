import pytest
from stschema.base.device import DeviceError
from stschema.base.util import ErrorEnum


class TestBaseDeviceError(object):
    def test_class_documentation(self):
        assert DeviceError
        assert DeviceError.__doc__
        assert len(DeviceError.__doc__)

    def test_error_instance(self):
        result = DeviceError(error_enum='DEVICE-UNAVAILABLE', detail='device out of range')
        assert isinstance(result, DeviceError)
        assert isinstance(result.error_enum, ErrorEnum)
        assert result.error_enum.name
        assert result.error_enum.value
        assert result.detail

    def test_value_error(self):
        with pytest.raises(ValueError):
            result = DeviceError(error_enum='UNSUPPORTED-ENUM', detail='deice error detail')

    def test_type_error(self):
        with pytest.raises(TypeError):
            result = DeviceError()
