# This test module serves as a BlackTesting module for
# the SchemaResponse Interface which will handle the
# validation, instantiation and serialization of the Device
# Object into a readable JSON response.
import pytest
from stschema.schema_response import SchemaResponse
from stschema import SchemaDevice


class TestSchemaResponseInterface(object):
    """Test Suite on SchemaResponsoe class which
    provides a series of classmethods to implemented
    at the SchemaConnector class.

    These methods cover the three main schema responses:
    Discovery Response, State Refresh Response,
    Command Response respectively."""
    class TestClassAttributes:
        # Test case on construction and specific
        # attributes of the class.
        def test_documentation(self):
            assert SchemaResponse
            assert SchemaResponse.__doc__
            assert len(SchemaResponse.__doc__) != 0

        def test_public_methods(self):
            assert SchemaResponse
            assert SchemaResponse.discovery_response
            assert SchemaResponse.state_refresh_response
            assert SchemaResponse.command_response

        def test_private_methods(self):
            assert SchemaResponse._validate_schema_response
            assert SchemaResponse._discovery_response
            assert SchemaResponse._state_refresh_response
            assert SchemaResponse._command_response


    class TestDiscoveryWorkFlow:
        # Test case on discovery_response
        # resource from SchemaResponse class.
        def test_discovery_response(self):
            assert SchemaResponse.discovery_response([SchemaDevice()], 'request_id')

        # Testing DiscoveryResponse public classmethod.
        # This method will be handled by the
        # _validate_schema_response function and
        # after validating response data will proceed to
        # call _discovery_response private method and
        # instantiate and serialize a DiscoveryResponse
        # object.
        def test_type_error_devices_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=int(123456789), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=str('STRING_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=set({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=frozenset({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=dict(key='value'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=bytes(b'BYTES_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                # Devices argument passed is list
                # but, items are not instances of
                # SchemaDevices.
                SchemaResponse.discovery_response(devices=list([123, 456]), request_id=__name__)

        def test_type_error_request_id_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=int(123456789), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=set({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=frozenset({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=dict(key='value'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=bytes(b'BYTES_ARG'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(request_id=list([123, 456]), devices=[SchemaDevice()])


    class TestStateRefreshWorkFlow:
        # Testing state_refresh_response public classmethod.
        # This method will be handled by the _validate_schema_response
        # function and after validating response will proceed to
        # call the _state_refresh_response to instantiate and
        # serialize a state_refresh_response object.
        def test_type_error_devices_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=int(123456789), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=str('STRING_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=set({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=frozenset({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=dict(key='value'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=bytes(b'BYTES_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                # Devices argument passed is list
                # but, items are not instances of
                # SchemaDevices.
                SchemaResponse.state_refresh_response(devices=list([123, 456]), request_id=__name__)

        def test_type_error_request_id_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=int(123456789), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=set({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=frozenset({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=dict(key='value'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=bytes(b'BYTES_ARG'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(request_id=list([123, 456]), devices=[SchemaDevice()])


    class TestCommandWorkFlow:
        # Testing command_response public classmethod.
        # This method will be handled by the _validate_schema_response
        # function and after validating data will proceed to
        # call the _command_response to instantiate aand
        # serialize a command_response object.
        def test_type_error_devices_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=int(123456789), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=str('STRING_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=set({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=frozenset({123, 456}), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=dict(key='value'), request_id=__name__)
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=bytes(b'BYTES_ARG'), request_id=__name__)
            with pytest.raises(TypeError):
                # Devices argument passed is list
                # but, items are not instances of
                # SchemaDevices.
                SchemaResponse.command_response(devices=list([123, 456]), request_id=__name__)

        def test_type_error_request_id_argument(self):
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=int(123456789), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=set({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=frozenset({123, 456}), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=dict(key='value'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=bytes(b'BYTES_ARG'), devices=[SchemaDevice()])
            with pytest.raises(TypeError):
                SchemaResponse.command_response(request_id=list([123, 456]), devices=[SchemaDevice()])
