import pytest
from stschema.interface.schemas import DeviceErrorSchema


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
        assert schema.fields['externalDeviceId']
        assert schema.fields['deviceError']

    def test_key_error_composition(self, schema):
        with pytest.raises(KeyError):
            assert schema
            assert schema.fields['deviceCookie']
            assert schema.fields['CREDENTIALS']
            assert schema.fields['PASSWORD']
            assert schema.fields['ERROR']
            assert schema.fields['SECRET']