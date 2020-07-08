# This test module serves as a BlackTesting module for
# the SchemaResponse Interface which will handle the
# validation, instantiation and serialization of the Device
# Object into a readable JSON response.
import pytest
from stschema.interface.schema_response import SchemaResponse
from stschema import Device

class TestSchemaResponseInterface(object):
    @pytest.fixture
    def dtypes(self):
        dtypes = [
            str('string'),
            int(666),
            float(99.9),
            bool(1),
            set(['one', 'two']),
            dict(one=1, two=2),
            None
        ]
        yield dtypes

    def test_schema_connector_documentation(self):
        assert SchemaResponse
        assert SchemaResponse.__doc__
        assert len(SchemaResponse.__doc__) != 0

    def test_schema_connector_composition(self):
        assert SchemaResponse
        assert SchemaResponse._schema_validator
        assert SchemaResponse.discovery_response
        assert SchemaResponse._discovery_response
        assert SchemaResponse.state_refresh_response
        assert SchemaResponse._state_refresh_response
        assert SchemaResponse.command_response
        assert SchemaResponse._command_response

    # This test will demonstrate the most basic use of the
    # response handlers.
    def test_responses_happy_path(self):
        assert SchemaResponse.discovery_response([Device()], 'request_id')
        assert SchemaResponse.state_refresh_response([Device()], 'request_id')
        assert SchemaResponse.command_response([Device()], 'request_id')

    # Testing DiscoveryResponse public classmethod.
    # This method will be handled by the _schema_validator
    # function and after validating data will proceed to
    # call the _discovery_response and instantiate a
    # serialize a DiscoveryResponse object.
    #
    # Applying different datatypes as devices argument.
    def test_discovery_response_type_error_devices(self, dtypes):
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=dt, request_id=__name__)
    # Applying different datatypes as request_id argument
    def test_discovery_response_type_error_request_id(self, dtypes):
        dtypes.pop(0) # Popint string datatype
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.discovery_response(devices=[Device()], request_id=dt)

    # Testing state_refresh_response public classmethod.
    # This method will be handled by the _schema_validator
    # function and after validating data will proceed to
    # call the _state_refresh_response and instantiate a
    # serialize a state_refresh_response object.
    #
    # Applying different datatypes as devices argument.
    def test_state_refresh_response_type_error_devices(self, dtypes):
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=dt, request_id=__name__)
    # Applying different datatypes as request_id argument
    def test_state_refresh_response_type_error_request_id(self, dtypes):
        dtypes.pop(0) # Popint string datatype
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.state_refresh_response(devices=[Device()], request_id=dt)

    # Testing command_response public classmethod.
    # This method will be handled by the _schema_validator
    # function and after validating data will proceed to
    # call the _command_response and instantiate a
    # serialize a command_response object.
    #
    # Applying different datatypes as devices argument.
    def test_command_response_type_error_devices(self, dtypes):
        # Applying different datatypes as devices argument.
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=dt, request_id=__name__)

    # Applying different datatypes as request_id argument
    def test_command_response_type_error_request_id(self, dtypes):
        dtypes.pop(0) # Popint string datatype
        for dt in dtypes:
            with pytest.raises(TypeError):
                SchemaResponse.command_response(devices=[Device()], request_id=dt)
