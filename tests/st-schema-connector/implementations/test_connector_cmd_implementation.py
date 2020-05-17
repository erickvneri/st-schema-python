import pytest
import hashlib
from datetime import datetime
from tests.fixtures import DeviceFixture
from stschema import SchemaConnector


class TestCommandResponseImplementation(object):
    @pytest.fixture
    def command_response(self) -> [DeviceFixture]:
        """Full implementation fixture of a CommandResponse"""
        d1 = DeviceFixture()
        d1.external_device_id = 'ONE'
        d2 = DeviceFixture()
        d2.external_device_id = 'TWO'
        d3 = DeviceFixture()
        d3.external_device_id = 'THREE'
        connector = SchemaConnector(devices=[d1, d2, d3])

        cmd = dict(
            externalDeviceId='TWO',
            deviceCookie={'cookie': datetime.now().strftime('%Y/%m/%d %H:%M:%:S')},
            commands=[{
                "component": "main",
                "capability": "st.colorControl",
                "command": "setColor",
                "arguments": [
                    {
                        "saturation": 91,
                        "hue": 0.8333333333333334
                    }]
            }]
        )
        command_response = connector.command_handler(
            command_device=cmd, request_id=hashlib.md5(b'requestId').hexdigest()
        )
        yield command_response

    def test_command_response_composition(self, command_response):
        assert command_response
        assert command_response['headers']
        assert command_response['deviceState']

    def test_command_response_headers(self, command_response):
        assert command_response
        assert command_response['headers']
        assert command_response['headers']['schema']
        assert command_response['headers']['version']
        assert command_response['headers']['requestId']
        assert command_response['headers']['interactionType']

    def test_command_response_device_state(self, command_response):
        assert command_response
        assert command_response['deviceState']
        assert command_response['deviceState'][0]
        assert type(command_response['deviceState']) is list
        assert type(command_response['deviceState'][0]) is dict
        assert len(command_response['deviceState'][0]) >= 1

    def test_key_error_command_response(self, command_response):
        with pytest.raises(KeyError):
            assert command_response['credentials']
            assert command_response['password']
            assert command_response['client_id']
            assert command_response['client_secret']
            assert command_response['code']
            assert command_response['authToken']
