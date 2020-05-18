from enum import Enum


class CapabilityAttribute(Enum):
    """The Capability Enum keeps
    relation between capabilities and
    its main attribute.

    For more information, please read the
    Capabilities Reference documentation:
    https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html
    """

    acceleration = 'st.accelerationSensor'
    battery = 'st.battery'
    button = 'st.button'
    color = 'st.colorControl'
    contact = 'st.contactSensor'
    coolingSetpoint = 'st.thermostatCoolingSetpoint'
    door = 'st.doorControl'
    motion = 'st.motionSensor'
    switch = 'st.switch'
    level = 'st.switchLevel'
    temperature = 'st.temperatureMeasurement'
    windowShade = 'st.windowShade'
