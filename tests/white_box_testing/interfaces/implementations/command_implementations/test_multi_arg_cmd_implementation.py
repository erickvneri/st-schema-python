import pytest
from stschema.base.device import BaseState
from stschema.interface import CommandHandler


class TestMultiArgCommand(object):
    @pytest.fixture
    def multi_arg_cmd(self):
        cmd = dict(
            component='main',
            capability='st.colorControl',
            command='setColor',
            arguments=[{
                'saturation': 99,
                'hue': 66
            }]
        )
        yield cmd

    def test_multi_arg_instance(self, multi_arg_cmd):
        handled_cmd = CommandHandler(multi_arg_cmd).get_state()
        assert type(handled_cmd) is list
        assert len(handled_cmd) != 0
        assert isinstance(handled_cmd[0], BaseState)
        assert isinstance(handled_cmd[1], BaseState)
        assert handled_cmd[0].attribute is 'saturation' or 'hue'
        assert handled_cmd[1].attribute is 'saturation' or 'hue'

