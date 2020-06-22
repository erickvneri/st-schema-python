import pytest
from tests.fixtures import DeviceFixture
from stschema.interface.schema_response.schemas import DeviceStateSchema
from stschema.base.device import BaseState


class TestStateImplementation(object):
    """This Test class will test the reliability of
    data and format for the information passed in a
    StateRefreshResponse."""

    @pytest.fixture
    def device(self):
        d = DeviceFixture()
        yield d

    @pytest.fixture
    def state_schema(self):
        schema = DeviceStateSchema()
        yield schema

    def test_state_fixture_instance(self, device):
        assert device
        assert device.states or device.states == []
        assert type(device.states) is list
        if len(device.states):
            assert isinstance(device.states[0], BaseState)

    def test_state_base_implementation(self, state_schema, device):
        state_result = state_schema.dump(device)
        assert state_result
        assert type(state_result) is dict
        assert type(state_result['states']) is list
        assert state_result['externalDeviceId']
        assert state_result['deviceCookie']
        assert state_result['states'] or state_result['states'] == []

    def test_state_capability_prefix(self, state_schema, device):
        prefix = 'st.'
        state_result = state_schema.dump(device)
        assert state_result
        for state in state_result['states']:
            assert state['capability'].startswith(prefix)
