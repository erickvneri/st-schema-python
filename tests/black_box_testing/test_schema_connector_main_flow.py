import pytest
import hashlib
from datetime import datetime
from stschema import SchemaConnector
from stschema.interface import Device
from tests.fixtures import DeviceFixture


class TestMainSchemaConnectorHandlers(object):
    """This Test class will test the
    reliability of attributes passed to
    avoid  side effects on instances. Also
    will test the main handlers of the
    SchemaConnector class."""

    @pytest.fixture
    def device(self):
        d = DeviceFixture()
        d.external_device_id = 'ONE'
        d2 = DeviceFixture()
        d2.external_device_id = 'TWO'
        d3 = DeviceFixture()
        d3.external_device_id = 'THREE'
        yield [d, d2, d3]

    @pytest.fixture
    def connector(self, device):
        connector = SchemaConnector(device)
        yield connector

    def test_elements_consistency(self, connector, device):
        """Device Fixture == device inside
        into SchemaConnector"""
        assert isinstance(connector.devices[0], DeviceFixture)
        assert isinstance(connector.devices[0], Device)
        assert isinstance(device[0], Device)
        assert isinstance(device[0], DeviceFixture)

    def test_discovery_response(self, connector, device):
        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        handler_result = connector.discovery_handler(request_id=req_id)
        for res_device in handler_result['devices']:
            assert res_device
            assert res_device['externalDeviceId']
            assert res_device['friendlyName']
            assert res_device['deviceUniqueId']
            assert res_device['deviceHandlerType']
            assert res_device['deviceCookie']
            assert res_device['deviceContext']
            assert res_device['manufacturerInfo']

    def test_state_refresh_response(self, connector, device):
        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        handler_result = connector.state_refresh_handler(devices=[{'externalDeviceId': 'ONE'}], request_id=req_id)
        assert handler_result['deviceState']
        assert len(handler_result['deviceState']) == 1

    def test_command_handler(self, connector, device):
        """Test to fail to guarantee that the
        device's states aren't being cleared and
        the command response is a shallow copy
        device response."""

        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        # Mock request of "devices to command"
        cmd = [dict(
            externalDeviceId='ONE',
            deviceCookie={'cookie': datetime.now().strftime('%Y/%m/%d %H:%M:%:S')},
            commands=[{
                "component": "main",
                "capability": "st.switch",
                "command": "on",
                "arguments": []
            }]
        )]
        handler_result = connector.command_handler(devices=cmd, request_id=req_id)
        res_state = handler_result['deviceState'][0]['states']
        assert len(res_state) == 1  # One state as response to CommandRequest
        assert len(device[0].states) == 3  # States of fixture hasn't being changed
        assert len(device[1].states) == 3  # States of fixture hasn't being changed
        assert len(device[2].states) == 3  # States of fixture hasn't being changed
