import pytest
from stschema.base import DeviceContext, DeviceContextSchema

class TestDeviceContext:
    @pytest.fixture
    def device_context(self):
        d_context = DeviceContext(room_name='Kitchen', groups=['home', 'kitchen'], categories=['light'])
        yield d_context

    @pytest.fixture
    def context_schema(self):
        schema = DeviceContextSchema()
        yield schema

    def test_class_construction(self):
        assert DeviceContext.__doc__
        assert len(DeviceContext.__doc__) != 0

    def test_schema_class_construction(self):
        assert DeviceContextSchema.__doc__
        assert len(DeviceContextSchema.__doc__) != 0

    def test_device_context_instance(self, device_context):
        assert device_context
        assert isinstance(device_context, DeviceContext)
        assert device_context.room_name
        assert device_context.groups
        assert device_context.categories
        assert type(device_context.room_name) is str
        assert type(device_context.groups) is list
        assert type(device_context.categories) is list

    def test_device_context_schema(self, device_context, context_schema):
        result_context = context_schema.dump(device_context)
        assert result_context
        assert result_context['roomName'] == 'Kitchen'
        assert result_context['groups'] == ['home', 'kitchen']
        assert result_context['categories'] == ['light']
