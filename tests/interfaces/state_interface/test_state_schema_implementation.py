import pytest
from stschema.interface import DeviceStateSchema
from tests.fixtures import StateFixture


class TestStateSchema:
    @pytest.fixture
    def device_state(self):
        fixture = StateFixture()
        yield fixture

    @pytest.fixture
    def schema(self):
        yield DeviceStateSchema()

    def test_schema_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_construction(self, schema):
        assert schema
        assert schema.fields['externalDeviceId']
        assert schema.fields['deviceCookie']
        assert schema.fields['states']

    def test_state_base_implementation(self, schema, device_state):
        state_result = schema.dump(device_state)
        assert state_result
        assert type(state_result) is dict
        assert state_result['externalDeviceId']
        assert state_result['deviceCookie']
        assert state_result['states'] or state_result['states'] == []

    def test_state_implementation_states(self, schema, device_state):
        state_result = schema.dump(device_state)
        assert state_result
        assert state_result['states']
        assert type(state_result['states']) is list
        assert len(state_result['states']) != 0

