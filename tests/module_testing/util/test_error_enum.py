import pytest
from stschema.util import StateErrorEnum


class TestStateErrorEnum(object):
    def test_enum_documentation(self):
        assert StateErrorEnum
        assert StateErrorEnum.__doc__
        assert len(StateErrorEnum.__doc__) != 0

    def test_enum_instance(self):
        assert StateErrorEnum('DEVICE-DELETED')
        assert StateErrorEnum('RESOURCE-CONSTRAINT-VIOLATION')
        assert StateErrorEnum('DEVICE-UNAVAILABLE')
        assert StateErrorEnum('CAPABILITY-NOT-SUPPORTED')

    def test_value_error(self):
        with pytest.raises(ValueError):
            assert StateErrorEnum('PASSWORD')
            assert StateErrorEnum('CREDENTIAL')
            assert StateErrorEnum('CLIENT_SECRET')
            assert StateErrorEnum('SECRET')
