from datetime import datetime
from pystschema import DeviceInterface

class DeviceFixture(DeviceInterface):
    """The DeviceFixture is a Testing Implementation
    to check the DiscoverySchema interface. This is
    just a test serialization. Mock Response. Etc."""

    def __init__(
        self, external_device_id='x123', friendly_name='Bath room', device_unique_id='a1b2c3',
        device_cookie=None, device_handler_type='c2c-rgb-bulb'
    ):
        DeviceInterface.__init__(
            self, external_device_id, friendly_name, device_unique_id, device_cookie, device_handler_type
        )

        self.set_context(
            room_name='Home', groups=['light', 'room'], categories=['light', 'bath']
        )
        self.set_mn(
            manufacturer_name='SmartThings', model_name='BulbDeluxe', hw_version='v1 MX 1.0', sw_version='0.1.0'
        )

        date_cookie = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.set_cookie(cookie=date_cookie)
