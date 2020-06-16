import pytest
from marshmallow import pprint
from datetime import datetime
from stschema import SchemaConnector, Device


connector = SchemaConnector()

class TestExploratory:
    @pytest.fixture
    def devices(self):
        d = Device(external_device_id='ONE')
        # with pytest.raises(ValueError):
        d.set_error_state(error_enum='', detail='deleted by user')
        devices = []
        devices.append(d)
        yield devices

    def test_discovery_exploration(self, devices):
        res = connector.command_response(devices=devices, request_id='2njlk4q32tq34nj')
        pprint(res)
