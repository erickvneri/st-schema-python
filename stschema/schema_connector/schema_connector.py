from stschema.schema_connector.response import (DiscoveryResponse, StateResponse,
                                                DiscoveryResponseSchema, StateRefreshResponseSchema)


class SchemaConnector:
    """The SchemaConnector class is the main
    API interface. It handles the instantiation
    and serialization of the discoveryResponse,
    stateRefreshResponse and commandResponse.
        ::: devices: list of Device instances."""

    @staticmethod
    def discovery_response(devices: list, request_id: str):
        """Returns discoveryResponse JSON
            :::param devices
            :::param request_id"""

        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    @staticmethod
    def state_refresh_response(devices: list, request_id: str):
        """Returns stateRefreshREsponse  JSON.
        If devices passed has deviceError state,
        it will be handled properly.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(devices=devices, request_id=request_id)
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)

    @staticmethod
    def command_response(devices: list, request_id: str):
        """Returns commandResponse JSON.
        If devices passed has deviceError state,
        it will be handled properly.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(devices=devices, request_id=request_id, interaction_type='commandResponse')
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)
