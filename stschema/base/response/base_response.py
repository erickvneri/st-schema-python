from .util import BaseHeaders


class BaseResponse(object):
    """The BaseResponse class inherit the
    attributes from the BaseHeaders class.
    It handles the instantiation of the
    response of the following requests:
        - discoveryRequest
        - stateRefreshResponse
        - commandRequest"""

    devices = []
    device_state = []

    def __init__(self, interaction_type: str, request_id: str):
        self.headers = BaseHeaders(interaction_type=interaction_type, request_id=request_id)
