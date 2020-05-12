import pytest
from stschema.interface import CommandHandler


class TestCommandInterface(object):
    @pytest.fixture
    def command_interface(self):
        yield CommandHandler

    def test_class_documentation(self, command_interface):
        assert command_interface
        assert command_interface.__doc__
        assert len(command_interface.__doc__) != 0

    def test_command_instance(self, command_interface):
        st_cmd = dict(component='main', capability='st.switchLevel', command='setLevel', arguments=[66])
        cmd = command_interface(st_cmd)
        assert cmd
        assert cmd.component
        assert cmd.capability
        assert cmd.command
        assert cmd.arguments
        print(cmd.__dict__)

    def test_command_instance_method_documentation(self, command_interface):
        assert command_interface
        assert command_interface.get_state
        assert command_interface.get_state.__doc__
        assert len(command_interface.get_state.__doc__) != 0
