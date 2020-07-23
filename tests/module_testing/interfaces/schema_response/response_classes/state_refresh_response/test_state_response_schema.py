import pytest
from stschema.schema_response.responses import StateRefreshResponseSchema


class TestStateRefreshResponse(object):
    """This class will test the composition and
    reliability of data and format of the
    StateRefreshResponseSchema class."""

    @pytest.fixture
    def schema(self):
        schema = StateRefreshResponseSchema()
        yield schema

    def test_schema_documentation(self, schema):
        assert schema
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_composition(self, schema):
        assert schema
        assert schema.fields['headers']
        assert schema.fields['deviceState']

    def test_key_error_composition(self, schema):
        with pytest.raises(KeyError):
            assert schema.fields['password']
            assert schema.fields['secret']
            assert schema.fields['clientSecret']
            assert schema.fields['clientId']
            assert schema.fields['secretKey']
            assert schema.fields['dbPassword']
