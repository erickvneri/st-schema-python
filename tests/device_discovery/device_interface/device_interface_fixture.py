from datetime import datetime
from pystschema import DeviceInterface

class DeviceFixture(DeviceInterface):
    """The DeviceFixture is a Testing Implementation
    to check the DiscoverySchema interface. This is
    just a test serialization. Mock Response. Etc."""

    def __init__(
        self, external_device_id='x1', device_cookie=None, friendly_name='Kitchen',
        device_handler_type='c2c', device_unique_id='123abc'
    ):
        DeviceInterface.__init__(
            self, external_device_id, device_cookie, friendly_name, device_unique_id, device_handler_type
        )

        self.set_context(
            room_name='Kitchen', groups=['light', 'fridge'], categories=['illumination']
        )
        self.set_mn(
            manufacturer_name='home expedit', model_name='self device', hw_version='v1 MX 1.0', sw_version='0.1.0'
        )

        date_cookie = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.set_cookie(cookie=date_cookie)
