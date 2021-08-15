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
import enum


class StateErrorEnum(enum.Enum):
    """
    The StateErrorEnum represents
    the supported device error states
    enumerators.
    """

    CAPABILITY_NOT_SUPPORTED = "CAPABILITY-NOT-SUPPORTED"
    DEVICE_DELETED = "DEVICE-DELETED"
    DEVICE_UNAVAILABLE = "DEVICE-UNAVAILABLE"
    RESOURCE_CONSTRAINT_VIOLATION = "RESOURCE-CONSTRAINT-VIOLATION"


class GlobalErrorEnum(enum.Enum):
    """
    The GlobalErrorEnum represents
    the supported global-context error
    enumerators.
    """

    BAD_REQUEST = "BAD-REQUEST"
    INTEGRATION_DELETED = "INTEGRATION-DELETED"
    INVALID_CLIENT = "INVALID-CLIENT"
    INVALID_CLIENT_SECRET = "INVALID-CLIENT-SECRET"
    INVALID_CODE = "INVALID-CODE"
    INVALID_INTERACTION_TYPE = "INVALID-INTERACTION-TYPE"
    INVALID_TOKEN = "INVALID-TOKEN"
    TOKEN_EXPIRED = "TOKEN-EXPIRED"
    UNSUPPORTED_GRANT_TYPE = "UNSUPPORTED-GRANT-TYPE"
