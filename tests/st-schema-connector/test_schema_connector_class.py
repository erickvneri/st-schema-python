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

    def test_schema_connector_composition(self, connector):
        assert connector
        assert connector.discovery_handler
        assert connector.state_refresh_handler
        assert connector.command_handler
