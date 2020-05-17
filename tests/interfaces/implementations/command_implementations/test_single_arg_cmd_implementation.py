import pytest
from stschema.base.device import BaseState
from stschema.interface import CommandHandler


class TestSingleArgCommand(object):
    @pytest.fixture
    def single_arg_command(self):
        cmd = dict(
            component='main',
            capability='st.thermostatCoolingSetpoint',
            command='setCoolingSetpoint',
            arguments=[69]
        )
        yield cmd

    def test_single_arg_instance(self, single_arg_command):
        handled_cmd = CommandHandler(single_arg_command).get_state()
        assert isinstance(handled_cmd, BaseState)
        assert handled_cmd
        assert handled_cmd.component
        assert handled_cmd.capability
        assert handled_cmd.attribute
        assert handled_cmd.value
        # assert handled_cmd.unit or handled_cmd.unit is None

    def test_value_error_capability(self, single_arg_command):
        """ValueError exception raised if
        Schema Connector receives capability
        without "st." prefix"""
        single_arg_command['capability'] = single_arg_command['capability'].lstrip('st.')
        with pytest.raises(ValueError):
            handled_cmd = CommandHandler(single_arg_command).get_state()


