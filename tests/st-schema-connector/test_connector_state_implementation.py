import pytest
import hashlib
from tests.fixtures import DeviceFixture
from stschema import SchemaConnector


class TestStateResponseImplementation(object):
    """This test will verify the reliability of the
    final ST Schema Connector interface, focusing on
    the StateRefreshResponse"""

    @pytest.fixture
    def state_refresh_response(self):
        mock_req_id = hashlib.md5(b'requestId').hexdigest()
        device = DeviceFixture()
        device.external_device_id = 'UNO'
        device2 = DeviceFixture()
        device2.external_device_id = 'DOS'
        device3 = DeviceFixture()
        device3.external_device_id = 'TRES'
        devices = [device, device2, device3]
        response = SchemaConnector.state_refresh_handler(devices=devices, request_id=mock_req_id)
        yield response

    def test_schema_connector_state_response(self, state_refresh_response):
        assert state_refresh_response
        assert state_refresh_response['headers']
        assert state_refresh_response['deviceState']

    def test_state_response_headers_composition(self, state_refresh_response):
        assert state_refresh_response
        assert state_refresh_response['headers']
        assert state_refresh_response['headers']['schema'] == 'st-schema'
        assert state_refresh_response['headers']['interactionType'] == 'stateRefreshResponse'
        assert state_refresh_response['headers']['version'] == '1.0'
        assert state_refresh_response['headers']['requestId']

    def test_state_response_device_state_composition(self, state_refresh_response):
        assert state_refresh_response
        assert state_refresh_response['deviceState']
        assert type(state_refresh_response['deviceState']) is list
        assert len(state_refresh_response['deviceState']) != 0
        assert state_refresh_response['deviceState'][0]
        assert state_refresh_response['deviceState'][0]['externalDeviceId']
        assert state_refresh_response['deviceState'][0]['deviceCookie']
        assert state_refresh_response['deviceState'][0]['deviceCookie']['cookie']
        assert state_refresh_response['deviceState'][0]['states']
        assert type(state_refresh_response['deviceState'][0]['states']) is list
        assert len(state_refresh_response['deviceState'][0]['states']) != 0
        assert state_refresh_response['deviceState'][0]['states'][0]
        assert state_refresh_response['deviceState'][0]['states'][0]['component']
        assert state_refresh_response['deviceState'][0]['states'][0]['capability']
        assert state_refresh_response['deviceState'][0]['states'][0]['attribute']
        assert state_refresh_response['deviceState'][0]['states'][0]['value']
        assert state_refresh_response['deviceState'][0]['states'][0]['unit'] or None

    def test_key_error_state_refresh_response(self, state_refresh_response):
        with pytest.raises(KeyError):
            assert state_refresh_response['credentials']
            assert state_refresh_response['password']
            assert state_refresh_response['client_id']
            assert state_refresh_response['client_secret']
            assert state_refresh_response['code']
            assert state_refresh_response['authToken']
