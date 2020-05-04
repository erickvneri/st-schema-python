import pytest
from stschema.responses import DiscoveryResponseSchema


class TestDiscoverySchema:
    """This class will test the composition and
    reliability of data and format of the
    DiscoveryResponseSchema class"""

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
            assert schema_class.fields['password']
            assert schema_class.fields['secret']
            assert schema_class.fields['clientSecret']
            assert schema_class.fields['clientId']
            assert schema_class.fields['secretKey']
            assert schema_class.fields['dbPassword']
