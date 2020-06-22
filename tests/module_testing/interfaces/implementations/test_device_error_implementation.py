import pytest
from tests.fixtures import DeviceFixture
from stschema.interface.device.schemas import DeviceErrorSchema
from stschema.base.device import DeviceError


class TestDeviceErrorImplementation(object):
    @pytest.fixture
    def device(self):
        d = DeviceFixture()
        d.set_error_state(error_enum='DEVICE-UNAVAILABLE', detail='out of range')
        yield d

    @pytest.fixture
    def err_schema(self):
        schema = DeviceErrorSchema()
        yield schema

    def test_device_instance_parent_classes(self, device):
        assert device
        assert isinstance(device.device_error[0], DeviceError)

    def test_device_error_instance(self, device):
        assert device
        assert device.external_device_id
        assert device.device_error
        assert type(device.device_error) is list
        assert device.device_error[0].error_enum
        assert device.device_error[0].detail

    def test_schema_implementation(self, device, err_schema):
        result = err_schema.dump(device)
        assert result
        assert result['externalDeviceId']
        assert result['deviceError']

    def test_key_error_schema_implementation(self, device, err_schema):
        result = err_schema.dump(device)
        with pytest.raises(KeyError):
            assert result['states']
            assert result['deviceCookie']