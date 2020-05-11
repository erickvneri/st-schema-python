import pytest
from enum import Enum


class TestVoidCommandEnum(object):
    @pytest.fixture
    def cmd_enum(self):
        class VoidCommand(Enum):
            """The VoidCommand Enumerator class is
            designed for commands that doesn't support
            additional values as arguments when receiving
            a CommandRequest interaction type."""
            on = 'on'
            off = 'off'
            open = 'open'
            closed = 'close'
        yield VoidCommand

    def test_enum_documentation(self, cmd_enum):
        assert cmd_enum
        assert cmd_enum.__doc__
        assert len(cmd_enum.__doc__) != 0

    def test_enum_instances(self, cmd_enum):
        switch_cmd_on = cmd_enum('on')
        switch_cmd_off = cmd_enum('off')
        door_cmd_open = cmd_enum('open')
        door_cmd_close = cmd_enum('close')
        assert switch_cmd_on
        assert switch_cmd_on.name
        assert switch_cmd_on.value
        assert switch_cmd_off
        assert switch_cmd_off.name
        assert switch_cmd_off.value
        assert door_cmd_open
        assert door_cmd_open.name
        assert door_cmd_open.value
        assert door_cmd_close
        assert door_cmd_close.name
        assert door_cmd_close.value

    def test_type_error(self,cmd_enum):
        with pytest.raises(ValueError):
            cmd_enum('not')
            cmd_enum('cicle')
            cmd_enum('code')
            cmd_enum('identify')
