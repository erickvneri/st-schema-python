import pytest
from stschema import SchemaConnector


class TestSchemaConnector(object):
    @pytest.fixture
    def connector(self):
        yield SchemaConnector

    def test_schema_connector_documentation(self, connector):
        assert connector
        assert connector.__doc__
        assert len(connector.__doc__) != 0

    def test_schema_connector_type_error(self, connector):
        with pytest.raises(TypeError):
            assert connector(credentials='cred:pass')
            assert connector(password='12345')
            assert connector(secret='secret')
            assert connector(client_secret='1-2aSbs_sd')

    def test_schema_connector_composition(self, connector):
        assert connector
        assert connector.discovery_handler
        assert connector.state_refresh_handler
        assert connector.command_handler

    def test_attribute_error_composition_schema_connector(self, connector):
        with pytest.raises(AttributeError):
            assert connector.not_supported_method
            assert connector.get_credentials
            assert connector.get_free_token
            assert connector.password
