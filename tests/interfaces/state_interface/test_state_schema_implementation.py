import pytest
from stschema.interface import DeviceStateSchema
from tests.fixtures import StateFixture


class TestStateSchema(object):
    """This class will test the StateFixture.
    It'll guarantee the data and format reliability
    according to a State Refresh Response main
    information."""

    @pytest.fixture
    def device_state(self):
        fixture = StateFixture()
        yield fixture

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

    def test_state_base_implementation(self, schema, device_state):
        state_result = schema.dump(device_state)
        assert state_result
        assert type(state_result) is dict
        assert type(state_result['states']) is list
        assert state_result['externalDeviceId']
        assert state_result['deviceCookie']
        assert state_result['states'] or state_result['states'] == []


