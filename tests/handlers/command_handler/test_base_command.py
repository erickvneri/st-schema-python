import pytest
from stschema.base.handlers import BaseCommand


class TestBaseCommandClass(object):
    @pytest.fixture
    def base_command(self):
        yield BaseCommand

    def test_class_documentation(self, base_command):
        assert base_command
        assert base_command.__doc__
        assert len(base_command.__doc__) != 0

    def test_class_instance(self, base_command):
        cmd = base_command(
            component='main',
            capability='st.colorControl',
            command='setColor',
            arguments=[{'saturation': 99, 'hue': 66}]
        )
        assert cmd
        assert isinstance(cmd, BaseCommand)
        assert cmd.component
        assert cmd.capability
        assert cmd.component
        assert cmd.arguments or []

    def test_class_type_error_null(self, base_command):
        with pytest.raises(TypeError):
            cmd = base_command()

    def test_class_type_error_extra_value(self, base_command):
        with pytest.raises(TypeError):
            cmd = base_command(
                component='main',
                capability='st.colorControl',
                command='setColor',
                arguments=[{'saturation': 99, 'hue': 66}],
                extra=0
            )
