from stschema import SchemaDevice


class SchemaDeviceFixture(SchemaDevice):
    """The SchemaDeviceFixture class is a Mock Device
    Implementation which handles the device info
    JSON that a DiscoveryResponse must contain."""

    def __init__(self, error_state: bool=False):
        SchemaDevice.__init__(self,
            'external_device_id',
            'friendly_name',
            'device_handler_type',
            'device_unique_id',
            'device_cookie'
        )
        # SETTING DEVICE CONTEXT
        self.set_context(
            'room_name',
            ['groups'],
            ['categories']
        )
        # SETTING MANUFACTURER INFORMATION
        self.set_mn(
            'manufacturer_info',
            'model_name',
            'hw_version',
            'sw_version'
        )
        # SETTING STATE OF THERMOSTAT DEVICE (CAPABILITY)
        self.set_state(
            'capability_1',
            'attribute',
            'value',
            'unit',
            'component'
        )
        self.set_state(
            'capability_2',
            'attribute',
            'value',
            None,
            'component'
        )
        self.set_state(
            'capability_3',
            'attribute',
            'value'
        )
        if error_state:
            self.set_error_state()
