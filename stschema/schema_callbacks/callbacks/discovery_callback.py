from stschema.schema_response.responses import DiscoveryResponse
from stschema.util.base_modules import BaseAuthentication


class DiscoveryCallback(DiscoveryResponse):
    def __init__(self, access_token: str, request_id: str, devices: list) -> 'DiscoveryCallback':
        DiscoveryResponse.__init__(
            self,
            devices=devices,
            request_id=request_id,
            interaction_type='discoveryCallback'
        )