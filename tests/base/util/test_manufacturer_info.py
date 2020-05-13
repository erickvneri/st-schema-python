import pytest
from stschema.base.device import ManufacturerInfo, ManufacturerSchema


class TestManufacturerInfo(object):
    """This test will be applied to the
        ManufacturerInfo class to guarantee its
        reliability in the data that the cloud
        requires"""

    @pytest.fixture
    def manufacturer(self):
        mn = ManufacturerInfo(
            manufacturer_name='SmartThings', model_name='SmartPlug', hw_version='v1 US Plug', sw_version='0.0.3'
        )
        yield mn

    @pytest.fixture
    def schema(self):
        schema = ManufacturerSchema()
        yield schema

    def test_manufacturer_class_documentation(self):
        assert ManufacturerInfo.__doc__
        assert len(ManufacturerInfo.__doc__) != 0

    def test_schema_class_documentation(self):
        assert ManufacturerSchema.__doc__
        assert len(ManufacturerSchema.__doc__) != 0

    def test_manufacturer_class_instance(self, manufacturer):
        assert manufacturer
        assert isinstance(manufacturer, ManufacturerInfo)
        assert manufacturer.manufacturer_name
        assert manufacturer.model_name
        assert manufacturer.hw_version
        assert manufacturer.sw_version

    def test_manufacturer_info_schema_instance(self, manufacturer, schema):
        mn_result = schema.dump(manufacturer)
        assert mn_result
        assert type(mn_result) is dict
        assert mn_result['manufacturerName']
        assert mn_result['modelName']
        assert mn_result['hwVersion']
        assert mn_result['swVersion']

    def test_manufacturer_schema_composition(self, schema):
        assert schema
        assert schema.fields['manufacturerName']
        assert schema.fields['modelName']
        assert schema.fields['hwVersion']
        assert schema.fields['swVersion']

    def test_type_error_instance_null_values(self):
        with pytest.raises(TypeError):
            mn = ManufacturerInfo()

    def test_type_error_instance_extra_value(self):
        with pytest.raises(TypeError):
            mn = ManufacturerInfo(
                manufacturer_name='SmartThings',
                model_name='SmartPlug',
                hw_version='v1 US Plug',
                sw_version='0.0.3',
                extra=0
            )
