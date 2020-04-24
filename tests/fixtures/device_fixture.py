from pystschema.interface import DeviceInterface
from datetime import datetime

class DeviceFixture(DeviceInterface):
    """The DeviceFixture class is a Mock Device
    Implementation which handles the device info
    JSON that a DiscoveryResponse must contain."""

    def __init__(self):
        DeviceInterface.__init__(
            self,
            external_device_id='9',
            friendly_name='BathLight',
            device_unique_id='dsfg7-654s',
            device_cookie=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            device_handler_type='c2c-bulb-rgb'
        )
        # SETTING DEVICE CONTEXT
        self.set_context(
            room_name='Home',
            groups=['light', 'room'],
            categories=['light', 'bath']
        )
        # SETTING MANUFACTURER INFORMATION
        self.set_mn(
            manufacturer_name='SmartThings',
            model_name='BulbDeluxe',
            hw_version='v1 MX 1.0', sw_version='0.1.0'
        )
