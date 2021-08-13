# MIT License
#
# Copyright (c) 2021 Erick Israel Vazquez Neri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
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

    def __init__(self, interaction_type: str, request_id: str) -> "BaseResponse":
        self.headers = BaseHeaders(
            interaction_type=interaction_type, request_id=request_id
        )
