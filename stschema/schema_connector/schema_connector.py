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
    discovery_schema = DiscoveryResponseSchema()
    state_schema = StateRefreshResponseSchema()

    def __init__(self, devices: List[Device]):
        self.devices = devices

    def discovery_handler(self, request_id: str):
        """Returns discoveryResponse JSON"""
        response = DiscoveryResponse(devices=self.devices, request_id=request_id)
        return self.discovery_schema.dump(response)

    def state_refresh_handler(self, devices: List[Device],  request_id: str = None):
        """Returns stateRefreshResponse JSON"""
        # SAVE
        # devices_req = [self.state_mapper.load(device)['external_device_id'] for device in devices]
        devices_req = [device['externalDeviceId'] for device in devices]
        devices_res = [device for device in self.devices if device.external_device_id in devices_req]

        response = StateResponse(devices=devices_res, request_id=request_id)
        return self.state_schema.dump(response)

    def command_handler(self, devices: List[Device], request_id: str):
        """Returns commandResponse"""
        # DeviceCommandMapper Schema mapping Command payload.
        command_req = self.command_mapper.load(devices[0])

        # Filter device by external_device_id
        device = copy(list(filter(lambda d: command_req['external_device_id'] == d.external_device_id, self.devices)).pop())

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
        return self.state_schema.dump(response)
