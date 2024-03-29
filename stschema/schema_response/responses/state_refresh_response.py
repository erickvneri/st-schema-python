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
from marshmallow import Schema, fields, pre_dump, post_dump
from stschema.util.base_modules import HeadersSchema, BaseResponse, AuthenticationSchema
from stschema.schema_device.schemas import DeviceStateSchema, DeviceErrorSchema

from pprint import pprint  # Delete line


class StateResponse(BaseResponse):
    """
    Inherits from the BaseResponse class.
    The StateResponse class handles the
    representation of the stateRefreshResponse.

        :::param headers
        :::param device_state
    """

    def __init__(
        self,
        devices: list,
        request_id: str,
        interaction_type: str = "stateRefreshResponse",
    ):
        BaseResponse.__init__(
            self, interaction_type=interaction_type, request_id=request_id
        )
        self.device_state = devices


class StateRefreshResponseSchema(Schema):
    """
    The StateRefreshResponseSchema handles
    the serialization of the StateResponse
    class supporting the nested
    DeviceStateSchema, HeadersSchema,
    DeviceErrorSchema, and AuthenticationSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    @pre_dump
    def _verify_dump(self, data, **kwargs):
        # Declare headers as required attribute.
        self.dump_fields.update(
            headers=fields.Nested(HeadersSchema, attribute="headers", required=True)
        )
        # Verify State instance attribute
        # If device_error at device instance,
        # DeviceErrorSchema will be used, else
        # DeviceStateSchema will be used.
        if data.device_state:
            if data.device_state[0].device_error:
                self.dump_fields.update(
                    deviceState=fields.List(
                        fields.Nested(DeviceErrorSchema), attribute="device_state"
                    )
                )
            else:
                self.dump_fields.update(
                    deviceState=fields.List(
                        fields.Nested(DeviceStateSchema), attribute="device_state"
                    )
                )
        # Verify Authentication non-required attribute.
        if data.authentication:
            self.dump_fields.update(
                authentication=fields.Nested(
                    AuthenticationSchema, attribute="authentication"
                )
            )
        return data

    @post_dump
    def _reset_device_state(self, data, **kwargs):
        # Reset deviceState to support
        # DeviceStateSchema as default
        # schema.
        self.dump_fields.update(
            deviceState=fields.List(
                fields.Nested(DeviceStateSchema), attribute="device_state"
            )
        )
        return data
