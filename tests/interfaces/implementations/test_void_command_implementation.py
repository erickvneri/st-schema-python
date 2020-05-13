import pytest
from stschema.interface import CommandHandler
from stschema.base.device import BaseState


class TestVoidCommand(object):
    @pytest.fixture
    def void_cmd_handler(self):
        cmd = dict(
            component='main',
            capability='st.doorControl',
            command='open',
            arguments=[]
        )
        handled_cmd = CommandHandler(cmd).get_state()
        yield handled_cmd

    def test_result_instance(self, void_cmd_handler):
        assert isinstance(void_cmd_handler, BaseState)
        assert void_cmd_handler
        assert void_cmd_handler.component
        assert void_cmd_handler.capability
        assert void_cmd_handler.attribute
        assert void_cmd_handler.value
        assert void_cmd_handler.unit or void_cmd_handler.unit is None
