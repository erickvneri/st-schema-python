import pytest
from stschema.base import BaseState
from marshmallow import Schema, fields


class TestDeviceState:
    @pytest.fixture
    def state_class(self):
        yield BaseState

    def test_class(self, state_class):
        assert state_class
        assert state_class.__init__

    def test_class_documentation(self, state_class):
        assert state_class.__doc__
        assert len(state_class.__doc__) != 0

    def test_class_definition(self, state_class):
        state = state_class(component='main', capability='switch', attribute='switch', value='off', unit=None)
        assert state
        assert isinstance(state, state_class)
        assert state.component
        assert state.capability
        assert state.attribute
        assert state.value
        assert state.unit or state.unit is None

    def test_bad_definition_missing_values(self, state_class):
        with pytest.raises(TypeError):
            assert state_class()

    def test_bad_definition_extra_value(self, state_class):
        with pytest.raises(TypeError):
            state = state_class(
                component='main', capability='switch', attribute='switch', value='off', unit=None, extra=None
            )

