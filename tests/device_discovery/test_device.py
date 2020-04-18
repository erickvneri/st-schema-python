import  pytest
from marshmallow import Schema, fields
from pystschema import Device, DeviceSchema

@pytest.fixture
def define_device():
    yield Device

@pytest.fixture
def device_schema():
    schema = DeviceSchema()
    yield schema

def test_device_definition(define_device):
    device_x = define_device(
        external_device_id='x1', device_cookie={}, friendly_name='fn', device_handler_type='c2c-bulb'
    )
    assert isinstance(device_x, define_device)
    assert device_x.external_device_id
    assert device_x.device_cookie is not None
    assert device_x.friendly_name
    assert device_x.device_handler_type

def test_dumped_device(define_device, device_schema):
    device_x = define_device(
        external_device_id='x1', device_cookie=None, friendly_name='fn', device_handler_type='c2c-bulb'
    )
    result_device = device_schema.dump(device_x)
    assert type(result_device) is dict
    assert result_device['friendly_name']
    assert result_device['external_device_id']
    assert result_device['device_cookie']
    assert result_device['device_handler_type']