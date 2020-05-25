from typing import List
from stschema.interface import Device, CommandHandler
from stschema.interface.schemas import DeviceCommandMapper
from stschema.schema_connector.response import DiscoveryResponse, StateResponse, ConnectorSchema


class SchemaConnector(object):
    """The SchemaConnector class is the main
    API interface. It handles the instantiation
    and serialization of the discoveryResponse,
    stateRefreshResponse and commandResponse.
        ::: devices: list of Device instances."""

    response_schema = ConnectorSchema()
    command_schema = DeviceCommandMapper()

    def __init__(self, devices: List[Device]):
        self.devices = devices

    def discovery_handler(self, request_id: str):
        """Returns discoveryResponse JSON"""
        response = DiscoveryResponse(devices=self.devices, request_id=request_id)
        return self.response_schema.dump(response)

    def state_refresh_handler(self, request_id: str):
        """Returns stateRefreshResponse JSON"""
        response = StateResponse(devices=self.devices, request_id=request_id)
        return self.response_schema.dump(response)

    def command_handler(self, command_device: List, request_id: str):
        """Returns commandResponse"""
        # DeviceCommandMapper Schema mapping Command payload.
        command_req = self.command_schema.load(command_device)

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
        return self.response_schema.dump(response)
