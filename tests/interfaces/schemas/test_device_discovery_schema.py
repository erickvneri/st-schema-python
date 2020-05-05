import pytest
from stschema.interface import DeviceDiscoverySchema


class TestDiscoverySchema(object):
    """This class guarantees the reliability of the
    data and format of a Discovery's device information"""

    @pytest.fixture
    def schema(self):
        schema = DeviceDiscoverySchema()
        yield schema

    def test_class_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_discovery_schema_composition(self, schema):
        assert schema
        assert schema.fields['externalDeviceId']
        assert schema.fields['friendlyName']
        assert schema.fields['deviceUniqueId']
        assert schema.fields['deviceCookie']
        assert schema.fields['deviceHandlerType']
        assert schema.fields['manufacturerInfo']

    def test_key_error_schema_composition(self, schema):
        with pytest.raises(KeyError):
            assert schema.fields['gate_way']
            assert schema.fields['password']
            assert schema.fields['client_secret']
            assert schema.fields['client_id']
            assert schema.fields['token']


