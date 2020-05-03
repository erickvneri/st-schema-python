import pytest
from stschema.responses import DiscoveryResponseSchema


class TestDiscoverySchema:
    @pytest.fixture
    def schema_class(self):
        schema = DiscoveryResponseSchema()
        yield schema

    def test_schema_documentation(self, schema_class):
        assert schema_class
        assert schema_class.__doc__
        assert len(schema_class.__doc__) != 0

    def test_schema_class(self, schema_class):
        assert schema_class
        assert schema_class.fields['devices']
        assert schema_class.fields['headers']

    def test_key_error(self, schema_class):
        with pytest.raises(KeyError):
            assert schema_class.fields['credentials']
            assert schema_class.fields['passwords']



