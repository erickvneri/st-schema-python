from stschema.util import BaseHeaders


class BaseResponse:
    """The BaseResponse represents the
    base information that will be extended
    in response to the following interaction
    types.
        - discoveryRequest
        - stateRefreshResponse
        - commandRequest
        - discoveryCallback
        - stateCallback
        - accessTokenRequest"""

    devices = []
    device_state = []

    def __init__(self, interaction_type: str, request_id: str) -> 'BaseResponse':
        self.headers = BaseHeaders(interaction_type=interaction_type, request_id=request_id)
