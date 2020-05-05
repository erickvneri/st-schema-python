from stschema.interface import Device
from datetime import datetime


class DeviceFixture(Device):
    """The DeviceFixture class is a Mock Device
    Implementation which handles the device info
    JSON that a DiscoveryResponse must contain."""

    def __init__(self):
        Device.__init__(
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
        # SETTING STATE OF THERMOSTAT DEVICE (CAPABILITY)
        self.set_state(
            capability='temperatureMeasurement',
            attribute='temperature',
            value=86,
            unit='F'
        )
        self.set_state(
            capability='waterSensor',
            attribute='water',
            value='dry'
        )
