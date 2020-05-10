import hashlib
import pytest
from tests.fixtures import DeviceFixture
from stschema import SchemaConnector


class TestSchemaConnectorImplementation(object):
    """This test will verify the reliability of the
    final ST Schema Connector interface, focusing on
    the StateRefreshResponse"""

    @pytest.fixture
    def discovery_response(self):
        mock_req_id = hashlib.md5(b'requestId').hexdigest()
        device = DeviceFixture()
        device.external_device_id = 'UNO'
        device2 = DeviceFixture()
        device2.external_device_id = 'DOS'
        device3 = DeviceFixture()
        device3.external_device_id = 'TRES'
        devices = [device, device2, device3]
        response = SchemaConnector.discovery_handler(devices=devices, request_id=mock_req_id)
        yield response

    def test_schema_connector_discovery_handler(self, discovery_response):
        assert discovery_response
        assert discovery_response['devices']
        assert discovery_response['headers']

    def test_discovery_response_headers_composition(self, discovery_response):
        assert discovery_response
        assert discovery_response['headers']
        assert discovery_response['headers']['schema'] == 'st-schema'
        assert discovery_response['headers']['version'] == '1.0'
        assert discovery_response['headers']['interactionType'] == 'discoveryResponse'
        assert discovery_response['headers']['requestId']

    def test_discovery_response_devices_composition(self, discovery_response):
        assert discovery_response
        assert discovery_response['devices']
        assert type(discovery_response['devices']) is list
        assert len(discovery_response['devices']) != 0
        assert discovery_response['devices'][0]['externalDeviceId']
        assert discovery_response['devices'][0]['deviceUniqueId']
        assert discovery_response['devices'][0]['friendlyName']
        assert discovery_response['devices'][0]['deviceCookie']
        assert discovery_response['devices'][0]['deviceCookie']['cookie']
        assert discovery_response['devices'][0]['manufacturerInfo']
        assert discovery_response['devices'][0]['manufacturerInfo']['swVersion']
        assert discovery_response['devices'][0]['manufacturerInfo']['hwVersion']
        assert discovery_response['devices'][0]['manufacturerInfo']['manufacturerName']
        assert discovery_response['devices'][0]['manufacturerInfo']['modelName']
        assert discovery_response['devices'][0]['deviceContext']['groups']
        assert discovery_response['devices'][0]['deviceContext']['roomName']
        assert discovery_response['devices'][0]['deviceContext']['categories']

    def test_key_error_discovery_response(self, discovery_response):
        with pytest.raises(KeyError):
            assert discovery_response['credentials']
            assert discovery_response['password']
            assert discovery_response['client_id']
            assert discovery_response['client_secret']
            assert discovery_response['code']
            assert discovery_response['authToken']
