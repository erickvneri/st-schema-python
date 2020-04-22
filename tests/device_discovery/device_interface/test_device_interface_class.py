import inspect
import pytest
from pystschema.base import BaseDevice
from pystschema import DeviceInterface

class TestDeviceInterface:
    @pytest.fixture
    def interface_class(self):
        yield DeviceInterface

    def test_class_documentation(self, interface_class):
        assert interface_class
        assert interface_class.__doc__
        assert len(interface_class.__doc__) != 0

    def test_interface_parent_class(self, interface_class):
        """This test will check if the parent class
        is actually the BaseDevice Class."""
        parent_class = inspect.getmro(interface_class)[1]
        assert parent_class == BaseDevice

    def test_interface_methods(self, interface_class):
        """Test that will check for defined
        interface methods."""
        assert interface_class.set_context
        assert interface_class.set_context.__doc__
        assert len(interface_class.set_context.__doc__) != 0
        assert interface_class.set_mn
        assert interface_class.set_mn.__doc__
        assert len(interface_class.set_mn.__doc__) != 0
        assert interface_class.set_cookie
        assert interface_class.set_cookie.__doc__
        assert len(interface_class.set_cookie.__doc__) != 0



