import pytest
from stschema.base import BaseState
from stschema.interface import DeviceStateInterface


class TestStateInterface(object):
    """This test will guarantee the reliability
    of the construction of the State Interface,
    which manages some device values and has
    instance methods to inject new capability state
    at the device's instance."""

    @pytest.fixture
    def interface_class(self):
        yield DeviceStateInterface

    @pytest.fixture
    def mock_state(self):
        state = DeviceStateInterface()
        yield state

    def test_class_documentation(self, interface_class):
        assert interface_class.__doc__
        assert len(interface_class.__doc__) != 0

    def test_state_interface_instance(self, mock_state):
        assert mock_state
        assert isinstance(mock_state, DeviceStateInterface)
        assert mock_state.external_device_id or mock_state.external_device_id is None
        assert mock_state.device_cookie or mock_state.device_cookie is None
        assert type(mock_state.states) is list

    class TestInstanceMethod(object):
        """This class will test the instance method:
            def set_state(
                component: str = 'main', capability: str, attribute: str, value: str or int, unit: str
            )"""

        def test_instance_method_set_state(self, interface_class):
            assert interface_class.set_state
            assert interface_class.set_state.__doc__
            assert len(interface_class.set_state.__doc__) != 0

        def test_type_error_instance_method_null_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_state()

        def test_type_error_instance_method_extra_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_state(
                    capability='temperatureMeasurement',
                    attribute='temperature',
                    value=350,
                    unit='F',
                    extra=0
                )

        def test_set_state_instance_method(self, mock_state):
            """The device/capability state that has been included
            in the StateInterface instance will be a instance of
            the BaseState class."""

            mock_state.set_state(
                capability='temperatureMeasurement',
                attribute='temperature',
                value=350,
                unit='F'
            )
            assert len(mock_state.states) != 0
            assert isinstance(mock_state.states[0], BaseState)
            assert mock_state.states[0].component
            assert mock_state.states[0].capability
            assert mock_state.states[0].attribute
            assert mock_state.states[0].value
            assert mock_state.states[0].unit or mock_state.states[0].unit is None

