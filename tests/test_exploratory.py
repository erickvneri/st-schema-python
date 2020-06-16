import pytest
from marshmallow import pprint
from datetime import datetime
from stschema import SchemaConnector
from tests.fixtures import DeviceFixture


connector = SchemaConnector()

class Test:
    @pytest.fixture
    def devices(self):
        d = DeviceFixture()
        d.external_device_id = 'ONE'
        d.set_error_state(error_enum='DEVICE-DELETED', detail='deleted by user')
        devices = []
        devices.append(d)
        yield devices

    def test_discovery_exploration(self, devices):
        req_devices = [{'externalDeviceId':'ONE'}]
        res = connector.state_refresh_handler(devices=devices, request_id='2njlk4q32tq34nj')
        pprint(res)