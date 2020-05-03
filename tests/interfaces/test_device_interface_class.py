import inspect
import pytest
from stschema.base import BaseDevice
from stschema.interface import Device


class TestDeviceInterface(object):
    """This test will verify the composition of the
        DiscoveryFixture."""

    @pytest.fixture
    def interface_class(self):
        yield Device

    def test_interface_parent_class(self, interface_class):
        """This test will check if the parent class
        is the BaseDevice Class."""
        parent_class = inspect.getmro(interface_class)[1]
        assert parent_class == BaseDevice

    def test_class_documentation(self, interface_class):
        assert interface_class
        assert interface_class.__doc__
        assert len(interface_class.__doc__) != 0

    class TestSetContextMethod(object):
        """This nested Test Class will test the instance
        method set_context, which will elaborate the
        device context information to the instantiated
        Device."""

        def test_set_context_interface_method_documentation(self, interface_class):
            assert interface_class.set_context
            assert interface_class.set_context.__doc__
            assert len(interface_class.set_context.__doc__) != 0

        def test_type_error_set_context_method(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_context()

        def test_type_error_set_context_method_extra_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_context(
                    room_name='Home',
                    groups=['light', 'room'],
                    categories=['light', 'bath'],
                    extra=0
                )

    class TestSetManufacturerMethod(object):
        """This nested Test Class will test the instance
        method set_mn, which will elaborate the device
        manufacturer information to the instantiated
        Device."""

        def test_set_mn_interface_method_documentation(self, interface_class):
            assert interface_class.set_mn
            assert interface_class.set_mn.__doc__
            assert len(interface_class.set_mn.__doc__) != 0

        def test_type_error_set_mn_method_null_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_mn()

        def test_type_error_set_mn_method_extra_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_mn(
                    manufacturer_name='SmartThings',
                    model_name='BulbDeluxe',
                    hw_version='v1 MX 1.0',
                    sw_version='0.1.0',
                    extra=0
                )

    class TestSetStateMethod(object):
        """This nested Test Class will test the instance
        method set_state, which will elaborate the device
        manufacturer information to the instantiated
        Device."""

        def test_set_state_interface_method_documentation(self, interface_class):
            assert interface_class
            assert interface_class.__doc__
            assert len(interface_class.__doc__) != 0

        def test_type_error_set_state_method_null_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_state()

        def test_type_error_set_state_method_extra_values(self, interface_class):
            with pytest.raises(TypeError):
                interface_class.set_state(
                    capability='temperatureMeasurement',
                    attribute='temperature',
                    value=86,
                    unit='F',
                    extra=0
                )
