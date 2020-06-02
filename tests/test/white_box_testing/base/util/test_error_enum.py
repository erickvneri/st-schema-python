import pytest
from stschema.base.util import ErrorEnum


class TestErrorEnum(object):
    def test_enum_documentation(self):
        assert ErrorEnum
        assert ErrorEnum.__doc__
        assert len(ErrorEnum.__doc__) != 0

    def test_enum_instance(self):
        assert ErrorEnum('DEVICE-DELETED')
        assert ErrorEnum('RESOURCE-CONSTRAINT-VIOLATION')
        assert ErrorEnum('DEVICE-UNAVAILABLE')
        assert ErrorEnum('CAPABILITY-NOT-SUPPORTED')
        assert ErrorEnum('TOKEN-EXPIRED')
        assert ErrorEnum('INTEGRATION-DELETED')
        assert ErrorEnum('BAD-REQUEST')
        assert ErrorEnum('INVALID-TOKEN')
        assert ErrorEnum('INVALID-INTERACTION-TYPE')
        assert ErrorEnum('UNSUPPORTED-GRANT-TYPE')
        assert ErrorEnum('INVALID-CODE')
        assert ErrorEnum('INVALID-CLIENT-SECRET')
        assert ErrorEnum('INVALID-CLIENT')

    def test_value_error(self):
        with pytest.raises(ValueError):
            assert ErrorEnum('PASSWORD')
            assert ErrorEnum('CREDENTIAL')
            assert ErrorEnum('CLIENT_SECRET')
            assert ErrorEnum('SECRET')
