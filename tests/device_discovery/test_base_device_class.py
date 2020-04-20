import  pytest
from pystschema import BaseDevice, DeviceSchema, DeviceCookie, DeviceCookieSchema

class TestSTDevice:
    # Define DeviceCookie for its use across the test.
    cookie = DeviceCookie.issue()
    cookie_schema = DeviceCookieSchema()
    device_cookie = cookie_schema.dump(cookie)

    @pytest.fixture
    def device_instance(self):
        device_instance = BaseDevice(
            external_device_id='x1', device_cookie=self.device_cookie,
            friendly_name='Hello World', device_handler_type='c2c-test'
        )
        yield device_instance

    @pytest.fixture
    def device_schema(self):
        schema = DeviceSchema()
        yield schema

    def test_class_construction(self):
        assert BaseDevice.__doc__
        assert len(BaseDevice.__doc__) != 0

    def test_schema_construction(self):
        assert DeviceSchema.__doc__
        assert len(DeviceSchema.__doc__) != 0

    def test_device_definition(self, device_instance):
        """This test will verify the main functionality
        of  the BaseDevice class."""
        assert isinstance(device_instance, BaseDevice)
        assert device_instance.external_device_id
        assert device_instance.device_cookie is not None
        assert device_instance.friendly_name
        assert device_instance.device_handler_type

    def test_alt_definition(self):
        with pytest.raises(TypeError):
            device_instance = BaseDevice()
            device_instance.external_device_id = 'x1'
            device_instance.device_cookie = self.device_cookie
            device_instance.friendly_name = 'fn'
            device_instance.device_handler_type = 'c2c-test'
            assert device_instance.external_device_id
            assert device_instance.device_cookie is not None
            assert device_instance.friendly_name
            assert device_instance.device_handler_type

    def test_device_schema(self, device_instance, device_schema):
        """This test will verify that the DeviceSchema
        is returning the serialization of the BaseDevice
        instance and that it is parsing its keys into
        a CamelCase format."""
        device_result = device_schema.dump(device_instance)
        assert device_result
        assert type(device_result) is dict
        assert type(device_result['deviceCookie']) is dict
        assert device_result['externalDeviceId']
        assert device_result['friendlyName']
        assert device_result['deviceCookie']
        assert device_result['deviceHandlerType']