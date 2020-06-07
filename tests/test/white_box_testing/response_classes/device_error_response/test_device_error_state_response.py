import pytest
import hashlib
from marshmallow import pprint
from tests.fixtures import DeviceFixture
from stschema.schema_connector.response import DeviceErrorResponseSchema, StateResponse


class TestDeviceErrorResponse(object):
    @pytest.fixture
    def error_state_response(self):
        # Request Id
        req_id = hashlib.md5(b'das3456sad534').hexdigest()
        # Device Instance with error state
        device = DeviceFixture()
        device.set_error_state(error_enum='DEVICE-DELETED', detail='device deleted by user')
        # State
        state_response = StateResponse(devices=[device], request_id=req_id)
        schema = DeviceErrorResponseSchema()
        yield schema.dump(state_response)

    def test_error_state_response_headers(self, error_state_response):
        assert error_state_response
        assert error_state_response['headers']
        assert error_state_response['headers']['schema']
        assert error_state_response['headers']['requestId']
        assert error_state_response['headers']['version']
        assert error_state_response['headers']['interactionType']
        assert error_state_response['headers']['interactionType'] == 'stateRefreshResponse'

    def test_error_state_response_device_state(self, error_state_response):
        assert error_state_response
        assert error_state_response['deviceState']
        assert error_state_response['deviceState'][0]['deviceError']
        assert error_state_response['deviceState'][0]['deviceError']
        assert error_state_response['deviceState'][0]['deviceError'][0]['errorEnum']
        assert error_state_response['deviceState'][0]['deviceError'][0]['detail']

    def test_error_state_key_error(self, error_state_response):
        with pytest.raises(KeyError):
            assert error_state_response['deviceState'][0]['states']
