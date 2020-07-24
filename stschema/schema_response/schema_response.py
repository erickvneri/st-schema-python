from stschema.schema_device import SchemaDevice
from stschema.schema_response.responses import (
    StateResponse,
    StateRefreshResponseSchema,
    DiscoveryResponse,
    DiscoveryResponseSchema
)


class SchemaResponse:
    """The SchemaResponse class handles
    the instantiation and serialization
    of the SchemaConnector JSON Responses."""

    @classmethod
    def discovery_response(cls, devices: list, request_id: str):
        """The discovery_response classmethod will handle
        the instantiation and serialization of the
        DiscoveryResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._validate_schema_response(devices, request_id, cls._discovery_response)

    @classmethod
    def state_refresh_response(cls, devices: list, request_id: str):
        """The state_refresh_response classmethod will
        handle the instantiation and serialization of the
        StateRefreshResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._validate_schema_response(devices, request_id, cls._state_refresh_response)

    @classmethod
    def command_response(cls, devices:list, request_id: str):
        """The command_response classmethod will handle
        the instantitation and serialization of a new
        State isntance in response of a Command Request.
            :::param devices: list of Device instances
            :::param request_id: str"""
        return cls._validate_schema_response(devices, request_id, cls._command_response)

    @staticmethod
    def _validate_schema_response(devices: list, request_id: str, response_callback):
        # This private classmethod will validate the data passed
        # to instantiate a DiscoveryResponse or StateRefreshResponse
        # (CommmandResponse).
        # It will enhance early development stages of Schema Connector
        # instances.
        if not isinstance(devices, list):
            raise TypeError('"devices" argument must be instance of list not %s' % type(devices))
        if devices:
            for device in devices:
                if not isinstance(device, SchemaDevice):
                    raise TypeError('"devices" items must be instances of %s, not %s' % (SchemaDevice, device))
        # Validate data type of request_id.
        # It must be string value
        if not isinstance(request_id, str):
            raise TypeError('request_id must be instance of str not %s' % type(request_id))
        return response_callback(devices, request_id)

    @staticmethod
    def _discovery_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a DiscoveryResponse and serialize it
        # into a readable JSON object.

        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    @staticmethod
    def _state_refresh_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a StateResponse and serialize it
        # into a readable JSON object.

        response = StateResponse(devices=devices, request_id=request_id)
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)

    @staticmethod
    def _command_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a command response(StateResponse)
        # and serialize it into a readable JSON object.

        response = StateResponse(
            devices=devices,
            request_id=request_id,
            interaction_type='commandResponse'
        )
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)

    @staticmethod
    def access_token_request(client_id: str, client_secret: str, code: str):
        raise NotImplementedError('Interaction resource not implemented.')

    @staticmethod
    def discovery_callback(devices: list, access_token: str):
        raise NotImplementedError('Interaction resource not implemented.')

    @staticmethod
    def state_callback(devices: list, access_token: str):
        raise NotImplementedError('Interaction resource not implemented.')
