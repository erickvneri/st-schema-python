import pytest
from stschema.base.device import BaseState, StateSchema


class TestStateSchema(object):
    """This test will guarantee the reliability in
    parsing and deserialize the State object as
    refers the ST Schema documentation"""

    @pytest.fixture
    def schema(self):
        yield StateSchema()

    @pytest.fixture
    def state_instance(self):
        instance = BaseState(component='main', capability='switch', attribute='switch', value='off', unit='F')
        yield instance

    def test_schema_class_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_schema_class_composition(self, schema):
        assert schema
        assert schema.fields['component']
        assert schema.fields['capability']
        assert schema.fields['attribute']
        assert schema.fields['value']
        assert schema.fields['unit']

    def test_schema_instance(self, schema, state_instance):
        state_result = schema.dump(state_instance)
        assert state_result
        assert type(state_result) is dict
        assert state_result['component']
        assert state_result['capability']
        assert state_result['attribute']
        assert state_result['value']
        assert state_result['unit']

    def test_null_unit_instance(self, schema):
        state_instance = BaseState(component='main', capability='switch', attribute='switch', value='off', unit=None)
        state_result = schema.dump(state_instance)
        with pytest.raises(KeyError):
            assert state_result['unit']