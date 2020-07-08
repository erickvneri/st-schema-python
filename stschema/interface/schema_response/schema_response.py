from stschema.interface.schema_response.responses import DiscoveryResponse, DiscoveryResponseSchema
from stschema.interface.schema_response.responses import StateResponse, StateRefreshResponseSchema
from stschema.interface.device import Device


class SchemaResponse:
    """The SchemaResponse class handles the instantiation
    and serialization of the SchemaConnector Http Responses."""

    @classmethod
    def discovery_response(cls, devices: list, request_id: str):
        """The discovery_response classmethod will handle
        the instantiation and serialization of the
        DiscoveryResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._schema_validator(devices, request_id, cls._discovery_response)

    @classmethod
    def state_refresh_response(cls, devices: list, request_id: str):
        """The state_refresh_response classmethod will
        handle the instantiation and serialization of the
        StateRefreshResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._schema_validator(devices, request_id, cls._state_refresh_response)

    @classmethod
    def command_response(cls, devices:list, request_id: str):
        """The command_response classmethod will handle
        the instantitation and serialization of a new
        State isntance in response of a Command Request.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._schema_validator(devices, request_id, cls._command_response)

    @staticmethod
    def _schema_validator(devices: list, request_id: str, response_callback):
        # This private classmethod will validate the data passed
        # to instantiate a DiscoveryResponse or StateRefreshResponse
        # (CommmandResponse).
        # It will enhance early development stages of Schema Connector
        # instances.
        if not isinstance(devices, list):
            raise TypeError('devices must be isntance of list.')
        if devices:
            for device in devices:
                if not isinstance(device, Device):
                    raise TypeError('devices items must be instances of %s, not %s' % (Device, device))
        # Validate data type of request_id.
        # It must be string value
        if not isinstance(request_id, str):
            raise TypeError('request_id must be instance of str')
        return response_callback(devices, request_id)


    @staticmethod
    def _discovery_response(devices: list, request_id: str):
        """This method creates the DiscoveryResponse
        class and call the correspondent Schema to serialize
        the Response object.
            :::param devices
            :::param request_id"""

        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)


    @staticmethod
    def _state_refresh_response(devices: list, request_id: str):
        """This method creates the StateRefreshResponse
        class and call the correspondent Schema to serialize
        the Response object.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(devices=devices, request_id=request_id)
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)

    @staticmethod
    def _command_response(devices: list, request_id: str):
        """This method creates a StateRefreshResponse in
        response of a Command Request.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(
            devices=devices,
            request_id=request_id,
            interaction_type='commandResponse'
        )
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)
