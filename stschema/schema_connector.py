from typing import List
from stschema.interface import Device
from stschema.responses import (DiscoveryResponse, StateResponse,
                                DiscoveryResponseSchema, StateRefreshResponseSchema)


class SchemaConnector(object):
    """The SchemaConnector class is the main
    API interface. It handles the instantiation
    and serialization of the DiscoveryResponse
    and StateResponse classes.

    It takes exclusive params to provide security
    and reliability at the Cloud-to-Cloud
    communication:

        :::param auth_url: None by  default.
        URL which will validate that the
        authorization token received is authorized.

        :::param save_access_code: False by default.
        If True, it will create a file to store the
        authorization code and stateCallback url received
        at the grantCallbackAccess interaction type.

        :::param logging: False by default. If True, a
        the SchemaConnector will instance a custom logger
        to improve the debugging experience."""

    # TODO: Implement actions of SchemaConnector.
    def __init__(
            self, auth_url: str = None, save_access_code: bool = False, logging: bool = False
    ):
        pass

    @staticmethod
    def discovery_handler(devices: List[Device], request_id: str):
        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    @staticmethod
    def state_refresh_handler(devices: List[Device], request_id: str):
        response = StateResponse(devices=devices, request_id=request_id)
        state_response = StateRefreshResponseSchema()
        return state_response.dump(response)

    @staticmethod
    def command_handler(request_id: str):
        pass
