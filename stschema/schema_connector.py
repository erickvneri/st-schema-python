from typing import List
from stschema.interface import Device, CommandHandler
from stschema.interface.schemas import DeviceCommandMapper
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

    command_mapper = DeviceCommandMapper()
    state_response = StateRefreshResponseSchema()

    # TODO: TBD SchemaConnector attributes.
    def __init__(
            self, devices: List[Device], save_access_code: bool = False, logging: bool = False
    ):
        self.devices = devices

    def discovery_handler(self, request_id: str):
        """Returns discoveryResponse JSON according to
        the SmartThings Schema Connector documentation"""
        response = DiscoveryResponse(devices=self.devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    def state_refresh_handler(self, request_id: str):
        response = StateResponse(devices=self.devices, request_id=request_id)
        """Returns stateRefreshResponse JSON according to
        the SmartThings Schema Connector documentation"""
        state_response = StateRefreshResponseSchema()
        return state_response.dump(response)

    def command_handler(self, command_device: List, request_id: str):
        """Returns commandResponse JSON according to
        the SmartThings Schema Connector documentation"""
        # DeviceCommandMapper Schema mapping Command payload.
        command_req = self.command_mapper.load(command_device)

        # Filter device by external_device_id
        device = list(filter(lambda d: command_req['external_device_id'] == d.external_device_id, self.devices)).pop()

        # CommandHandler to generate new state.
        handled_cmd = CommandHandler(command_req['commands'].pop()).get_state()

        # Clean states repository
        device.states = []
        if type(handled_cmd) is list:
            device.states = [state for state in handled_cmd]
        else:
            device.states.append(handled_cmd)

        # Instantiate StateResponse to handle command response
        response = StateResponse(devices=[device], request_id=request_id, interaction_type='commandResponse')
        return self.state_response.dump(response)
