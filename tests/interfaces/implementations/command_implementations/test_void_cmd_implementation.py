import pytest
from stschema.interface import CommandHandler
from stschema.base.device import BaseState


class TestVoidCommand(object):
    @pytest.fixture
    def void_cmd(self):
        cmd = dict(
            component='main',
            capability='st.doorControl',
            command='open',
            arguments=[]
        )
        yield cmd

    def test_result_instance(self, void_cmd):
        handled_cmd = CommandHandler(void_cmd).get_state()
        assert isinstance(handled_cmd, BaseState)
        assert handled_cmd
        assert handled_cmd.component
        assert handled_cmd.capability
        assert handled_cmd.attribute
        assert handled_cmd.value
        assert handled_cmd.unit or handled_cmd.unit is None

    def test_value_error_capability(self, void_cmd):
        """ValueError exception raised if
        Schema Connector receives capability
        without "st." prefix"""
        void_cmd['capability'] = void_cmd['capability'].lstrip('st.')
        with pytest.raises(ValueError):
            handled_cmd = CommandHandler(void_cmd).get_state()
