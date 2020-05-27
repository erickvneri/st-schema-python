import pytest
import hashlib
from datetime import datetime
from stschema import SchemaConnector
from stschema.interface import Device
from tests.fixtures import DeviceFixture


class TestMainFlow(object):
    """This Test class will test the
    reliability of attributes passed to
    avoid  side effects on instances. Also
    will test the main handlers of the
    SchemaConnector class."""

    @pytest.fixture
    def device(self):
        d = DeviceFixture()
        yield d

    @pytest.fixture
    def connector(self, device):
        connector = SchemaConnector([device])
        yield connector

    def test_elements_consistency(self, connector, device):
        """Device Fixture == device inside
        into SchemaConnector"""
        assert isinstance(connector.devices[0], DeviceFixture)
        assert isinstance(connector.devices[0], Device)
        assert isinstance(device, Device)
        assert isinstance(device, DeviceFixture)
        assert connector.devices[0] == device

    def test_discovery_response(self, connector, device):
        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        handler_result = connector.discovery_handler(request_id=req_id)
        res_device = handler_result['devices'].pop()
        assert res_device
        assert res_device['externalDeviceId'] == device.external_device_id
        assert res_device['friendlyName'] == device.friendly_name
        assert res_device['deviceUniqueId'] == device.device_unique_id
        assert res_device['deviceHandlerType'] == device.device_handler_type
        assert res_device['deviceCookie'] == device.device_cookie.__dict__

    def test_state_refresh_response(self, connector, device):
        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        handler_result = connector.state_refresh_handler(request_id=req_id)
        res_state = handler_result['deviceState'][0]['states']
        assert res_state
        assert len(res_state) == len(device.states)
        for i in range(len(res_state)):
            assert res_state[i] == device.states[i].__dict__

    def test_command_handler(self, connector, device):
        """Test to fail to guarantee that the
        device's states aren't being cleared and
        the command response is a shallow copy
        device response."""

        req_id = hashlib.sha3_256(b'fdsa63dfsa45f').hexdigest()
        cmd = dict(
            externalDeviceId='xaf0as8FASd2jkl',
            deviceCookie={'cookie': datetime.now().strftime('%Y/%m/%d %H:%M:%:S')},
            commands=[{
                "component": "main",
                "capability": "st.switch",
                "command": "on",
                "arguments": []
            }]
        )
        handler_result = connector.command_handler(command_device=cmd, request_id=req_id)
        res_state = handler_result['deviceState'][0]['states']
        assert len(res_state) == 1 # One state as response to CommandRequest
        assert len(device.states) == 3 # States of fixture hasn't being changed
