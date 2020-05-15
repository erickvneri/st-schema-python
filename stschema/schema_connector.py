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

        ::: devices: List of device instances.

        :::param save_access_code: False by default.
        If True, it will create a file to store the
        authorization code and stateCallback url received
        at the grantCallbackAccess interaction type.

        :::param logging: False by default. If True, a
        the SchemaConnector will instance a custom logger
        to improve the debugging experience."""

    # TODO: Implement actions of SchemaConnector.
    def __init__(
            self, devices: List[Device], save_access_code: bool = False, logging: bool = False
    ):
        self.devices = devices

    def discovery_handler(self, request_id: str):
        response = DiscoveryResponse(devices=self.devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    def state_refresh_handler(self, request_id: str):
        response = StateResponse(devices=self.devices, request_id=request_id)
        state_response = StateRefreshResponseSchema()
        return state_response.dump(response)

    @staticmethod
    def command_handler(command_device: List, request_id: str):
        """
        1. Filter device.
        2. Map Command - Get State.
        3. Instance StateResponse.
        4. Dump new state.
        """
        pass
