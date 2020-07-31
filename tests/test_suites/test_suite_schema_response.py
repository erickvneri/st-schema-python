# Test Suite over the SchemaResponse
# class and the serialization of the
# Discovery, State Response and Command
# Responses respectively.
#
# For this test suite, the fixtures used
# will be the following:
#   - device_fixture
#   - error_state_device_fixture
#   - discovery_response_fixture
#   - state_refresh_fixture
import pytest
from stschema import SchemaDevice
from stschema.schema_response import SchemaResponse
from tests.device_fixture import SchemaDeviceFixture
# Fixtures import
from tests.fixtures import (
    # Responses fixtures
    discovery_response_fixture,
    state_refresh_response_fixture,
    command_response_fixture,
    # SchemaDevice fixtures
    device_fixture,
    error_state_device,
    state_device,
    discovery_device
)


class TestSchemaResponseInterface(object):
    """Test Suite on SchemaResponsoe class which
    provides a series of classmethods to be
    implemented at the SchemaConnector class.

    These methods cover the three main schema responses:
    Discovery Response, State Refresh Response,
    Command Response respectively."""
    class TestSchemaResponseClassAttributes:
        # Test case on construction and specific
        # attributes of the class.
        def test_documentation(self):
            assert SchemaResponse
            assert SchemaResponse.__doc__

        def test_public_methods(self):
            assert SchemaResponse
            assert SchemaResponse.discovery_response
            assert SchemaResponse.state_refresh_response
            assert SchemaResponse.command_response
            assert SchemaResponse.global_error_response

        def test_private_methods(self):
            assert SchemaResponse._validate_schema_response
            assert SchemaResponse._discovery_response
            assert SchemaResponse._state_refresh_response
            assert SchemaResponse._command_response
            assert SchemaResponse._global_error_response


    class TestDiscoveryResponse:
        def test_discovery_response_documentation(self, discovery_response_fixture):
            assert discovery_response_fixture
            assert discovery_response_fixture.__doc__
        # Test case on discovery_response
        # resource from SchemaResponse class.
        def test_discovery_response(self, discovery_response_fixture, discovery_device):
            assert isinstance(discovery_response_fixture['headers'], dict)
            assert discovery_response_fixture['headers']['schema'] == 'st-schema'
            assert discovery_response_fixture['headers']['version'] == '1.0'
            assert discovery_response_fixture['headers']['requestId'] == 'request_id_example'
            assert discovery_response_fixture['headers']['interactionType'] == 'discoveryResponse'
            # discovery_device fixture is used to
            # verify that content of the
            # DiscoveryReponse follows the
            # content of a simple SchemaDevice
            # sesrialization.
            assert discovery_response_fixture['devices'][0] == discovery_device

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


    class TestStateRefreshResponse:
        def test_state_refresh_documentation(self, state_refresh_response_fixture):
            assert state_refresh_response_fixture
            assert state_refresh_response_fixture.__doc__
        # Test case on state_refresh_response
        # resource from SchemaResponse class.
        def test_state_refresh_response(self, state_refresh_response_fixture, state_device):
            assert isinstance(state_refresh_response_fixture['headers'], dict)
            assert state_refresh_response_fixture['headers']['schema'] == 'st-schema'
            assert state_refresh_response_fixture['headers']['version'] == '1.0'
            assert state_refresh_response_fixture['headers']['requestId'] == 'request_id_example'
            assert state_refresh_response_fixture['headers']['interactionType'] == 'stateRefreshResponse'
            # state_device fixture is used to
            # verify that content of the
            # StateRefreshResponse follows the
            # content of a simple SchemaDevice
            # sesrialization.
            assert state_refresh_response_fixture['deviceState'][0] == state_device

        # Test case on state_refresh_response
        # passing SchemaDevice with error_state
        # as True.
        def test_state_refresh_response_device_error(self, error_state_device):
            error_state_device = error_state_device[1]
            device_error_response = SchemaResponse.state_refresh_response([error_state_device], 'request_id_example')
            assert isinstance(device_error_response['headers'], dict)
            assert device_error_response['headers']['schema'] == 'st-schema'
            assert device_error_response['headers']['version'] == '1.0'
            assert device_error_response['headers']['requestId'] == 'request_id_example'
            assert device_error_response['headers']['interactionType'] == 'stateRefreshResponse'
            # DeviceError attributes
            device_error = device_error_response['deviceState'][0]['deviceError'][0]
            assert device_error['errorEnum'] == error_state_device.device_error[0].error_enum
            assert device_error['detail'] == error_state_device.device_error[0].detail
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


    class TestCommandResponse:
        def test_command_response_documentation(self, command_response_fixture):
            assert command_response_fixture
            assert command_response_fixture.__doc__

        # Test case on discovery_response
        # resource from SchemaResponse class.
        def test_command_response(self, command_response_fixture, state_device):
            assert command_response_fixture['headers']['schema'] == 'st-schema'
            assert command_response_fixture['headers']['version'] == '1.0'
            assert command_response_fixture['headers']['requestId'] == 'request_id_example'
            assert command_response_fixture['headers']['interactionType'] == 'commandResponse'
            # Since command responses are
            # updates of a State instance,
            # the state_device fixture is
            # used to compared data passed
            # as response.
            assert command_response_fixture['deviceState'][0] == state_device

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


    class TestGlobalError:
        def test_global_error_response_class_documentation(self):
            from stschema.schema_response.responses import (
                GlobalErrorResponse,
                GlobalErrorSchema
            )
            assert GlobalErrorResponse.__doc__
            assert GlobalErrorSchema.__doc__

        def test_global_error_handler_documentation(self):
            assert SchemaResponse.global_error_response
            assert SchemaResponse.global_error_response.__doc__

        # Test case on a GlobalError
        # response.
        def test_global_error_response_default(self):
            global_error_response = SchemaResponse \
                .global_error_response(
                    'interaction_type',
                    'request_id',
                )
            assert global_error_response
            assert global_error_response['headers']['requestId'] == 'request_id'
            assert global_error_response['headers']['interactionType'] == 'interaction_type'
            assert global_error_response['headers']['schema'] == 'st-schema'
            assert global_error_response['headers']['version'] == '1.0'
            assert global_error_response['globalError']
            assert global_error_response['globalError']['errorEnum'] == 'BAD-REQUEST'
            assert global_error_response['globalError']['detail'] == 'invalid request arguments.'

        def test_exception_errors_global_error_instance(self):
            with pytest.raises(TypeError):
                SchemaResponse.global_error_response()
            with pytest.raises(ValueError):
                SchemaResponse.global_error_response(
                    'interaction_type',
                    'request_id',
                    'UNSUPPORTED-ENUM'
                )
            with pytest.raises(TypeError):
                SchemaResponse.global_error_response(
                    'interaction_type',
                    'request_id',
                    'BAD-REQUEST',
                    'detail',
                    'UNEXPECTED_ARGUMENT'
                )
