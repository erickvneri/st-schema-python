import pytest
from stschema.base import BaseState, StateSchema


class TestStateSchema:
    @pytest.fixture
    def schema(self):
        yield StateSchema()

    @pytest.fixture
    def state_instance(self):
        instance = BaseState(component='main', capability='switch', attribute='switch', value='off', unit=None)
        yield instance

    def test_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_class(self, schema):
        assert schema
        assert schema.fields['component']
        assert schema.fields['capability']
        assert schema.fields['attribute']
        assert schema.fields['value']
        assert schema.fields['unit']

    def test_schema_with_state_instance(self, schema, state_instance):
        state_result = schema.dump(state_instance)
        assert state_result
        print(state_result)
        assert type(state_result) is dict
        assert state_result['component']
        assert state_result['capability']
        assert state_result['attribute']
        assert state_result['value']
        assert state_result['unit'] or state_result['unit'] is None
