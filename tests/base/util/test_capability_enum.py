import pytest
from stschema.base.util import CapabilityAttribute


class TestCapabilityEnum(object):
    @pytest.fixture
    def supported_capabilities(self):
        yield ['st.accelerationSensor', 'st.battery', 'st.button', 'st.colorControl',
               'st.contactSensor', 'st.thermostatCoolingSetpoint', 'st.doorControl', 'st.motionSensor',
               'st.switch', 'st.switchLevel', 'st.temperatureMeasurement', 'st.windowShade']

    def test_capability_documentation(self):
        assert CapabilityAttribute
        assert CapabilityAttribute.__doc__
        assert len(CapabilityAttribute.__doc__) != 0

    def test_supported_capabilities(self, supported_capabilities):
        for capability in supported_capabilities:
            assert CapabilityAttribute(capability)
            assert CapabilityAttribute(capability).name
            assert CapabilityAttribute(capability).value

    def test_error_not_supported_capabilities(self):
        with pytest.raises(ValueError):
            CapabilityAttribute('st.robotCleanerCleaningMode')
            CapabilityAttribute('st.robotCleanerMovement')
            CapabilityAttribute('st.robotCleanerTurboMode')

    def test_type_error(self):
        with pytest.raises(TypeError):
            CapabilityAttribute()
