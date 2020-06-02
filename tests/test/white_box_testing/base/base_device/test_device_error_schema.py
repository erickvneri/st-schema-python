import pytest
from stschema.base.device import DeviceErrorSchema, DeviceError


class TestDeviceErrorSchema(object):
    @pytest.fixture
    def schema(self):
        s = DeviceErrorSchema()
        yield s

    def test_schema_documentation(self, schema):
        assert schema
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_composition(self, schema):
        assert schema
        assert schema.fields['errorEnum']
        assert schema.fields['detail']

    def test_key_error_schema(self, schema):
        with pytest.raises(KeyError):
            assert schema.fields['credentials']
            assert schema.fields['secret']
            assert schema.fields['secret_client']
            assert schema.fields['code']
            assert schema.fields['access_token']

    def test_basic_implementation(self, schema):
        err = DeviceError('DEVICE-DELETED', 'device deleted by user')
        result = schema.dump(err)
        assert result
        assert result['errorEnum']
        assert result['detail']

    def test_key_error_implementation(self, schema):
        with pytest.raises(KeyError):
            err = DeviceError('DEVICE-UNAVAILABLE', 'device deleted by user')
            result = schema.dump(err)
            assert result
            assert result['CRED']
            assert result['PASS']
