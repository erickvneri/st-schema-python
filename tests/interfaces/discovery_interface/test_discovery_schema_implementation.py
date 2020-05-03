import pytest
from stschema.interface import DeviceSchema
from stschema.base import BaseCookie, DeviceContext, ManufacturerInfo
from tests.fixtures import DiscoveryFixture


class TestDiscoverySchema(object):
    """This class guarantees the reliability of the
    data and format of a Discovery's device information"""

    @pytest.fixture
    def schema(self):
        schema = DeviceSchema()
        yield schema

    @pytest.fixture
    def device_fixture(self):
        device = DiscoveryFixture()
        yield device

    def test_class_documentation(self, schema):
        assert schema.__doc__
        assert len(schema.__doc__) != 0

    def test_discovery_schema_composition(self, schema):
        assert schema
        assert schema.fields['externalDeviceId']
        assert schema.fields['friendlyName']
        assert schema.fields['deviceUniqueId']
        assert schema.fields['deviceCookie']
        assert schema.fields['deviceHandlerType']
        assert schema.fields['manufacturerInfo']

    def test_instance_parent_classes(self, device_fixture):
        assert isinstance(device_fixture.device_cookie, BaseCookie)
        assert isinstance(device_fixture.manufacturer_info, ManufacturerInfo)
        assert isinstance(device_fixture.device_context, DeviceContext)

    def test_discovery_fixture_instance(self, device_fixture):
        assert device_fixture
        assert device_fixture.external_device_id
        assert device_fixture.device_cookie
        assert device_fixture.friendly_name
        assert device_fixture.device_handler_type
        assert device_fixture.device_unique_id
        assert device_fixture.manufacturer_info

    def test_discovery_fixture_schema_instance(self, schema, device_fixture):
        device_result = schema.dump(device_fixture)
        assert schema
        assert device_result['externalDeviceId']
        assert device_result['friendlyName']
        assert device_result['deviceUniqueId']
        assert device_result['deviceCookie']
        assert device_result['deviceHandlerType']
        assert device_result['manufacturerInfo']
        assert device_result['deviceContext']
