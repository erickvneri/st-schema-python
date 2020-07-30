from stschema.schema_response.responses import StateResponse
from stschema.util import BaseAuthentication, AuthenticationSchema

class StateCallback(StateResponse):
    """
    The StateCallback class represents
    the information used to instance
    Device State Callbacks.
    """
    def __init__(self, access_token: str, request_id: str, devices: list) -> 'StateCallback':
        StateResponse.__init__(
            self,
            devices=devices,
            request_id=request_id,
            interaction_type='stateCallback'
        )
        self.authentication = BaseAuthentication(access_token)
