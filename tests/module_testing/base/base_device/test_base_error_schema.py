import pytest
from stschema.base.device import BaseErrorSchema, DeviceError


class TestDeviceErrorSchema(object):
    @pytest.fixture
    def schema(self):
        s = BaseErrorSchema()
        yield s

    def test_schema_documentation(self, schema):
        assert schema
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_composition(self, schema):
        assert schema
        assert len(schema.declared_fields) == 2
        assert schema.fields['errorEnum']
        assert schema.fields['detail']

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

