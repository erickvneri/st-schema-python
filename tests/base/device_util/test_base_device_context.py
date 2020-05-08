import pytest
from stschema.base.device import DeviceContext, DeviceContextSchema


class TestDeviceContext(object):
    """This test will be applied to the
    DeviceContext class to guarantee its
    reliability in the data that the cloud
    requires"""

    @pytest.fixture
    def device_context(self):
        d_context = DeviceContext(room_name='Kitchen', groups=['home', 'kitchen'], categories=['light'])
        yield d_context

    @pytest.fixture
    def context_schema(self):
        schema = DeviceContextSchema()
        yield schema

    def test_class_documentation(self):
        assert DeviceContext.__doc__
        assert len(DeviceContext.__doc__) != 0

    def test_schema_class_documentation(self):
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

    def test_device_context_schema_instance(self, device_context, context_schema):
        result_context = context_schema.dump(device_context)
        assert result_context
        assert result_context['roomName'] == 'Kitchen'
        assert result_context['groups'] == ['home', 'kitchen']
        assert result_context['categories'] == ['light']

    def test_device_context_schema_composition(self, context_schema):
        assert context_schema
        assert context_schema.fields['roomName']
        assert context_schema.fields['groups']
        assert context_schema.fields['categories']

    def test_type_error_instance_null_values(self):
        with pytest.raises(TypeError):
            context = DeviceContext()

    def test_type_error_instance_extra_values(self):
        with pytest.raises(TypeError):
            context = DeviceContext(room_name='Kitchen', groups=['home', 'kitchen'], categories=['light'], extra=0)


