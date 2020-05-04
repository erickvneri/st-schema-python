import pytest
from tests.fixtures import DeviceFixture
from stschema.interface import Device
from stschema.responses.util import Header
from stschema.responses import StateResponse, StateRefreshResponseSchema


class TestStateRefresh(object):
    @pytest.fixture
    def state_response(self):
        # Request ST Headers
        mock_req = dict(requestId='1j23n-1KJfs-f9Gk3')
        device = DeviceFixture()
        # State Refresh Instance
        state_res = StateResponse(
            devices=[device, device, device],
            request_id=mock_req['requestId']
        )
        yield state_res

    @pytest.fixture
    def schema(self):
        schema = StateRefreshResponseSchema()
        yield schema

    def test_class_documentation(self,state_response):
        assert state_response
        assert state_response.__doc__
        assert len(state_response.__doc__) != 0

    def test_state_response_instance(self, state_response):
        assert state_response
        assert state_response.device_state
        assert state_response.headers
        assert isinstance(state_response.headers, Header)

    def test_state_refresh_response(self, state_response, schema):
        state_result = schema.dump(state_response)
        assert state_result
        assert state_result['deviceState']
        assert state_result['headers']

    def test_key_error(self, state_response, schema):
        state_result = schema.dump(state_response)
        with pytest.raises(KeyError):
            assert state_result
            assert state_result['credentials']
            assert state_result['password']
            assert state_result['secret']
            assert state_result['secretKey']
            assert state_result['clientSecret']