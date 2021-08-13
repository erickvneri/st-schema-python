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
from stschema.schema_device import SchemaDevice
from stschema.util.base_modules import GlobalErrorEnum, BaseError
from stschema.schema_response.responses import (
    DiscoveryResponse,
    DiscoveryResponseSchema,
    StateResponse,
    StateRefreshResponseSchema,
    GlobalErrorResponse,
    GlobalErrorSchema,
)


class SchemaResponse:
    """
    The SchemaResponse class handles
    the instantiation and serialization
    of the SchemaConnector JSON Responses.
    """

    @classmethod
    def discovery_response(cls, devices: list, request_id: str):
        """
        The discovery_response classmethod will handle
        the instantiation and serialization of the
        DiscoveryResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str
        """
        return cls._validate_schema_response(
            devices, request_id, cls._discovery_response
        )

    @classmethod
    def state_refresh_response(cls, devices: list, request_id: str):
        """
        The state_refresh_response classmethod will
        handle the instantiation and serialization of the
        StateRefreshResponse into a readable JSON object
        response.
            :::param devices: list of Device instances
            :::param request_id: str
        """
        return cls._validate_schema_response(
            devices, request_id, cls._state_refresh_response
        )

    @classmethod
    def command_response(cls, devices: list, request_id: str):
        """
        The command_response classmethod will handle
        the instantitation and serialization of a new
        State isntance in response of a Command Request.
            :::param devices: list of Device instances
            :::param request_id: str
        """
        return cls._validate_schema_response(devices, request_id, cls._command_response)

    @staticmethod
    def _validate_schema_response(devices: list, request_id: str, response_callback):
        # This private classmethod will validate the data passed
        # to instantiate a DiscoveryResponse or StateRefreshResponse
        # (CommmandResponse).
        # It will enhance early development stages of Schema Connector
        # instances.
        if not isinstance(devices, list):
            raise TypeError(
                '"devices" argument must be instance of list not %s' % type(devices)
            )
        if devices:
            for device in devices:
                if not isinstance(device, SchemaDevice):
                    raise TypeError(
                        '"devices" items must be instances of %s, not %s'
                        % (SchemaDevice, device)
                    )
        # Validate data type of request_id.
        # It must be string value
        if not isinstance(request_id, str):
            raise TypeError(
                "request_id must be instance of str not %s" % type(request_id)
            )
        return response_callback(devices, request_id)

    @staticmethod
    def _discovery_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a DiscoveryResponse and serialize it
        # into a readable JSON object.

        response = DiscoveryResponse(devices=devices, request_id=request_id)
        discovery_schema = DiscoveryResponseSchema()
        return discovery_schema.dump(response)

    @staticmethod
    def _state_refresh_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a StateResponse and serialize it
        # into a readable JSON object.

        response = StateResponse(devices=devices, request_id=request_id)
        state_schema = StateRefreshResponseSchema()
        return state_schema.dump(response)

    @staticmethod
    def _command_response(devices: list, request_id: str):
        # Private method with the responsibility to
        # instantiate a command response(StateResponse)
        # and serialize it into a readable JSON object.

        response = StateResponse(
            devices=devices, request_id=request_id, interaction_type="commandResponse"
        )
        state_schema = StateRefreshResponseSchema()
        return state_schema.dump(response)

    @classmethod
    def global_error_response(
        cls,
        interaction_type: str,
        request_id: str,
        error_enum: str = "BAD-REQUEST",
        detail: str = "invalid request arguments.",
    ):
        """
        Defines a global error of communication
        between Clouds.
        Supported Global Error enumerators:
            - BAD-REQUEST
            - INTEGRATION-DELETED
            - INVALID-CLIENT
            - INVALID-CLIENT-SECRET
            - INVALID-CODE
            - INVALID-INTERACTION-TYPE
            - INVALID-TOKEN
            - TOKEN-EXPIRED
            - UNSUPPORTED-GRANT-TYPE

            :::param interaction_type (required)
            :::param request_id (required)
            :::param error_enum: "BAD-REQUEST" by default
            :::param detail: message or detail
            about global error.
        """
        try:
            error_enum = GlobalErrorEnum(error_enum)
        except ValueError as e:
            raise ValueError("Device error enumerator not supported: %s" % error_enum)
        else:
            if not request_id:
                raise TypeError('"request_id" argument is missing')
            else:
                global_error = BaseError(error_enum.value, detail)
                return cls._global_error_response(
                    interaction_type, request_id, global_error
                )

    @staticmethod
    def _global_error_response(*error_info):
        response = GlobalErrorResponse(error_info[0], error_info[1], error_info[2])
        error_schema = GlobalErrorSchema()
        return error_schema.dump(response)
