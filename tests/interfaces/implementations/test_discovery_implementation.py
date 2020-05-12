import pytest
from tests.fixtures import DeviceFixture
from stschema.interface import DeviceDiscoverySchema
from stschema.base.device import DeviceContext, ManufacturerInfo
from stschema.base.util import BaseCookie


class TestDiscoveryImplementation(object):
    """This Test class will test the reliability of
    data and format for the information passed in a
    DiscoveryResponse."""

    @pytest.fixture
    def device(self):
        d = DeviceFixture()
        yield d

    @pytest.fixture
    def schema(self):
        s = DeviceDiscoverySchema()
        yield s

    def test_instance_parent_classes(self, device):
        assert isinstance(device.device_cookie, BaseCookie)
        assert isinstance(device.manufacturer_info, ManufacturerInfo)
        assert isinstance(device.device_context, DeviceContext)

    def test_discovery_fixture_instance(self, device):
        assert device
        assert device.external_device_id
        assert device.device_cookie
        assert device.friendly_name
        assert device.device_handler_type
        assert device.device_unique_id
        assert device.manufacturer_info

    def test_discovery_fixture_schema_instance(self, schema, device):
        device_result = schema.dump(device)
        assert schema
        assert device_result['externalDeviceId']
        assert device_result['friendlyName']
        assert device_result['deviceUniqueId']
        assert device_result['deviceCookie']
        assert device_result['deviceHandlerType']
        assert device_result['manufacturerInfo']
        assert device_result['deviceContext']
