from stschema.util.base_modules import BaseHeaders


class BaseResponse:
    """
    The BaseResponse represents the
    base information that will be extended
    in response to the following interaction
    types.
        - discoveryRequest
        - stateRefreshResponse
        - commandRequest
        - discoveryCallback
        - stateCallback
        - accessTokenRequest
    """
    # Future implementation reference
    devices = list()
    device_state = list()
    authentication = dict()
    global_error = dict()

    def __init__(self, interaction_type: str, request_id: str) -> 'BaseResponse':
        self.headers = BaseHeaders(interaction_type=interaction_type, request_id=request_id)
