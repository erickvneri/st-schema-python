from stschema.interface import DiscoveryInterface
from datetime import datetime


class DiscoveryFixture(DiscoveryInterface):
    """The DeviceFixture class is a Mock Device
    Implementation which handles the device info
    JSON that a DiscoveryResponse must contain."""

    def __init__(self):
        DiscoveryInterface.__init__(
            self,
            external_device_id='xaf0as8FASd2jkl',
            friendly_name='ThermoSensor',
            device_unique_id='x11h2j4b2',
            device_cookie=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            device_handler_type='c2c-thermo-device-handler'
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
