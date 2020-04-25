import pytest
from pystschema.base import ManufacturerInfo, ManufacturerSchema

class TestManufacturerInfo:
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

    def test_manufacturer_class_construction(self):
        assert ManufacturerInfo.__doc__
        assert len(ManufacturerInfo.__doc__) != 0

    def test_schema_class_construction(self):
        assert ManufacturerSchema.__doc__
        assert len(ManufacturerSchema.__doc__) != 0

    def test_manufacturer_class(self, manufacturer):
        assert manufacturer
        assert isinstance(manufacturer, ManufacturerInfo)
        assert manufacturer.manufacturer_name
        assert manufacturer.model_name
        assert manufacturer.hw_version
        assert manufacturer.sw_version

    def test_manufacturer_info_schema(self, manufacturer, schema):
        mn_result = schema.dump(manufacturer)
        assert mn_result
        assert type(mn_result) is dict
        assert mn_result['manufacturerName']
        assert mn_result['modelName']
        assert mn_result['hwVersion']
        assert mn_result['swVersion']













