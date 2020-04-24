import pytest
from pystschema.discovery_implementation import DiscoverySchema
from tests.fixtures import DeviceFixture

class TestDiscoverySchema:
    @pytest.fixture
    def discovery_schema(self):
        schema = DiscoverySchema()
        yield schema

    @pytest.fixture
    def schema_class(self):
        yield DiscoverySchema()

    @pytest.fixture
    def device(self):
        device = DeviceFixture()
        yield device

    def test_schema_class(self, schema_class):
        assert schema_class
        assert schema_class.fields['devices']
        assert schema_class.fields['headers']

    def test_key_error(self, schema_class):
        with pytest.raises(KeyError):
            assert schema_class.fields['credentials']
            assert schema_class.fields['passwords']



