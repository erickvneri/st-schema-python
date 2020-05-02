from stschema.interface import DeviceStateInterface
from stschema.base import BaseCookie
from datetime import datetime


class StateFixture(DeviceStateInterface):
    """The StateFixture class is a quick test
    implementation of the Device States refered
    at the ST Schema/StateRefreshResponse
    documentation:
    https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/smartthings-schema-reference.html#State-Refresh"""

    def __init__(self):
        DeviceStateInterface.__init__(
            self,
            external_device_id='x102045ab'
        )

        updated_cookie = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.device_cookie = BaseCookie(updated_cookie)
        self.set_state(capability='switch', attribute='switch', value='off')
        self.set_state(capability='temperatureMeasurement', attribute='temperature', value=999, unit='F')
        self.set_state(capability='waterSensor', attribute='water', value='wet')
