from stschema.base import BaseState


class DeviceStateInterface:
    """The StateInterface class will handle the
    the construction of the main data of a device
    in a State Refresh Response:

        :::param external_device_id
        :::param device_cookie: by default the
        cookie previously set at the
        DiscoveryInterface's device.
        :::param device_state: a list that
        specify the state of each capability
        the device supports."""

    def __init__(self, **info):
        self.external_device_id = info.get('external_device_id')
        self.device_cookie = info.get('device_cookie')
        self.states = []

    def set_state(self, capability: str, attribute: str, value: str or int, component: str = 'main', unit: str = None):
        """The set_state method add a capability-state
        to the device that has been used passed to the
        StateInterface constructor.

        For more information about the capabilities
        supported, please visit the Capabilities
        Reference documentation:
        https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html"""

        new_state = BaseState(
            component=component,
            capability=capability,
            attribute=attribute,
            value=value,
            unit=unit
        )
        self.states.append(new_state)