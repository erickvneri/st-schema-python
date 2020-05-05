import pytest
from stschema.interface import DeviceStateSchema


class TestStateSchema(object):
    """This class will test the StateFixture.
    It'll guarantee the data and format reliability
    according to a State Refresh Response main
    information."""

    @pytest.fixture
    def schema(self):
        schema = DeviceStateSchema()
        yield schema

    def test_schema_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_composition(self, schema):
        assert schema
        assert schema.fields['externalDeviceId']
        assert schema.fields['deviceCookie']
        assert schema.fields['states']

    def test_key_error_schema_composition(self, schema):
        with pytest.raises(KeyError):
            assert schema.fields['credentials']
            assert schema.fields['port']
            assert schema.fields['hackable_info']



