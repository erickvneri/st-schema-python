import  pytest
import pystschema
from pystschema import Device, DeviceSchema, DeviceCookie, DeviceCookieSchema

class TestSTDevice:
    """The TestSTDevice will check for the
    main attributes for a SmartThings Device
    that has been integrated through the ST-Schema
    Connector.
        :::param external_device_id: device id for a
        third-party cloud.
        :::param friendly_name: Name set by the user.
        :::param device_handler_type: string  referred
        at the main ST-Schema documentation:
        https://smartthings.developer.samsung.com/docs//devices/smartthings-schema/device-handler-types.html
        :::param device_cookie: DeviceCookie object."""
    cookie = DeviceCookie.issue()
    cookie_schema = DeviceCookieSchema()
    device_cookie = cookie_schema.dump(cookie)

    @pytest.fixture
    def define_device(self):
        yield Device

    @pytest.fixture
    def device_schema(self):
        schema = DeviceSchema()
        yield schema

    def test_device_definition(self, define_device):

        device_x = define_device(
            external_device_id='x1', device_cookie=self.device_cookie,
            friendly_name='Hello World', device_handler_type='c2c-bulb'
        )
        assert isinstance(device_x, define_device)
        assert device_x.external_device_id
        assert device_x.device_cookie is not None
        assert device_x.friendly_name
        assert device_x.device_handler_type

    def test_dumped_device(self, define_device, device_schema):
        device_x = define_device(
            external_device_id='x1', device_cookie=self.device_cookie,
            friendly_name='Hello World', device_handler_type='c2c-bulb'
        )
        result_device = device_schema.dump(device_x)
        assert type(result_device) is dict
        assert result_device['friendly_name']
        assert result_device['external_device_id']
        assert result_device['device_cookie']
        assert result_device['device_handler_type']