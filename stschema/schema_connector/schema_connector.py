from typing import List
from copy import copy
from stschema.interface import Device, CommandHandler
from stschema.schema_connector.handler_schemas import DeviceCommandMapper
from stschema.schema_connector.response import (DiscoveryResponse, StateResponse,
                                                DiscoveryResponseSchema, StateRefreshResponseSchema)


class SchemaConnector(object):
    """The SchemaConnector class is the main
    API interface. It handles the instantiation
    and serialization of the discoveryResponse,
    stateRefreshResponse and commandResponse.
        ::: devices: list of Device instances."""

    command_mapper = DeviceCommandMapper()

    def __init__(self, devices: list = None):
        self.devices = devices

    def discovery_handler(self, devices: list, request_id: str):
        """Returns discoveryResponse JSON
            :::param devices
            :::param request_id"""

        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    def state_refresh_handler(self, devices: list, request_id: str):
        """Returns stateRefreshREsponse  JSON.
        If devices passed has deviceError state,
        it will be handled properly.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(devices=devices, request_id=request_id)
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)

    def command_handler(self, devices: list, request_id: str):
        """Returns commandResponse JSON.
        If devices passed has deviceError state,
        it will be handled properly.
            :::param: devices
            :::param: request_id"""

        response = StateResponse(devices=devices, request_id=request_id, interaction_type='commandResponse')
        state_schema = StateRefreshResponseSchema(states=response.device_state)
        return state_schema.dump(response)
