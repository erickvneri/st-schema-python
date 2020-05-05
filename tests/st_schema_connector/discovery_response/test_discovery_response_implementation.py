import pytest
from tests.fixtures import DeviceFixture
from stschema.responses import DiscoveryResponseSchema, DiscoveryResponse


class TestDiscoveryResponse:

    @pytest.fixture
    def discovery_response(self):
        # Request ST Headers
        mock_req = dict(requestId='1j23n-1KJfs-f9Gk3')
        # Device implementation
        device = DeviceFixture()
        discovery_response = DiscoveryResponse(devices=[device], request_id=mock_req['requestId'])
        yield discovery_response

    @pytest.fixture
    def schema(self):
        schema = DiscoveryResponseSchema()
        yield schema

    def test_class_documentation(self, discovery_response):
        assert discovery_response
        assert discovery_response.__doc__
        assert len(discovery_response.__doc__) != 0

    def test_discovery_response_instance(self, discovery_response):
        assert discovery_response
        assert discovery_response.devices
        assert type(discovery_response.devices) is list
        assert discovery_response.headers

    def test_type_error_discovery_response_instance_null_values(self):
        with pytest.raises(TypeError):
            discovery_error_instance = DiscoveryResponse()

    def test_type_error_discovery_response_instance_extra_values(self):
        with pytest.raises(TypeError):
            discovery_error_instance = DiscoveryResponse(devices=['device'], request_id='11bn23-fds', extra=0)

    def test_discovery_response_implementation(self, schema, discovery_response):
        discovery_result = schema.dump(discovery_response)
        assert discovery_result
        assert discovery_result['headers']
        assert type(discovery_result['headers']) is dict
        assert discovery_result['devices']
        assert type(discovery_result['devices']) is list

    def test_key_error_discovery(self, schema, discovery_response):
        discovery_result = schema.dump(discovery_response)
        with pytest.raises(KeyError):
            assert discovery_result
            assert discovery_result['credentials']
            assert discovery_result['password']
            assert discovery_result['secret']
            assert discovery_result['secretKey']
            assert discovery_result['clientSecret']
