import pytest
from stschema.base import BaseState
from stschema.interface import StateInterface


class TestStateInterface:
    @pytest.fixture
    def interface_class(self):
        """Raw class"""
        yield StateInterface

    @pytest.fixture
    def mock_state(self):
        """Simple instance"""
        state = StateInterface()
        yield state

    def test_class_documentation(self, interface_class):
        assert interface_class.__doc__
        assert len(interface_class.__doc__) != 0

    def test_state_interface_instance(self, mock_state):
        assert mock_state
        assert isinstance(mock_state, StateInterface)
        assert mock_state.external_device_id or mock_state.external_device_id is None
        assert mock_state.device_cookie or mock_state.device_cookie is None
        assert type(mock_state.device_state) is list

    def test_interface_method_set_state(self, interface_class):
        assert interface_class.set_state
        assert interface_class.set_state.__doc__
        assert len(interface_class.set_state.__doc__) != 0

    def test_set_state_instance_method(self, mock_state):
        """The state that has been included in the StateInterface
        instance will be a instance of the BaseState class."""

        mock_state.set_state(
            capability='temperatureMeasurement',
            attribute='temperature',
            value=350,
            unit='F'
        )
        assert len(mock_state.device_state) != 0
        assert isinstance(mock_state.device_state[0], BaseState)
        assert mock_state.device_state[0].component
        assert mock_state.device_state[0].capability
        assert mock_state.device_state[0].attribute
        assert mock_state.device_state[0].value
        mock_state.device_state[0].unit = None
        assert mock_state.device_state[0].unit or mock_state.device_state[0].unit is None

