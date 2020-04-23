import pytest
from pystschema import DiscoverySchema
from pystschema.base import BaseDeviceCookie, BaseDeviceContext, BaseManufacturer
from tests.device_discovery.device_interface.device_interface_fixture import DeviceFixture

class TestDiscoverySchema:
    @pytest.fixture
    def schema(self):
        schema = DiscoverySchema()
        yield schema

    @pytest.fixture
    def schema_class(self):
        yield DiscoverySchema

    @pytest.fixture
    def device_fixture(self):
        device = DeviceFixture()
        yield device

    def test_class_documentation(self, schema_class):
        assert schema_class.__doc__
        assert len(schema_class.__doc__) != 0

    def test_nested_classes(self, device_fixture):
        assert isinstance(device_fixture.device_cookie, BaseDeviceCookie)
        assert isinstance(device_fixture.manufacturer_info, BaseManufacturer)
        assert isinstance(device_fixture.device_context, BaseDeviceContext)

    def test_device_representation(self, device_fixture):
        assert device_fixture
        assert device_fixture.external_device_id
        assert device_fixture.device_cookie
        assert device_fixture.friendly_name
        assert device_fixture.device_handler_type
        assert device_fixture.device_unique_id
        assert device_fixture.manufacturer_info

    def test_device_schema(self, schema, device_fixture):
        device_result = schema.dump(device_fixture)
        assert schema
        assert device_result['externalDeviceId'] == device_fixture.external_device_id
        assert device_result['friendlyName'] == device_fixture.friendly_name
        assert device_result['deviceUniqueId'] == device_fixture.device_unique_id
        assert device_result['deviceCookie'] == device_fixture.device_cookie.__dict__
        assert device_result['deviceHandlerType'] == device_fixture.device_handler_type
        assert device_result['manufacturerInfo']
        assert device_result['deviceContext']
