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
from marshmallow import Schema, fields, pre_dump
from stschema.schema_device.schemas import DeviceDiscoverySchema
from stschema.util.base_modules import BaseResponse, HeadersSchema


class DiscoveryResponse(BaseResponse):
    """
    The DiscoveryResponse is an object
    representation in response to the
    "discoveryRequest" Interaction Type.
    Inherits from BaseResponse.

        :::param devices
        :::param request_id
    """

    def __init__(
        self,
        devices: list,
        request_id: str,
        interaction_type: str = "discoveryResponse",
    ) -> "DiscoveryResponse":
        BaseResponse.__init__(
            self, interaction_type=interaction_type, request_id=request_id
        )
        self.devices = devices


class DiscoveryResponseSchema(Schema):
    """
    The DiscoveryResponseSchema handles
    the serialization of the DiscoveryResponse
    class supporting the nested
    DeviceDiscoverySchema, HeadersSchema,
    and AuthenticationSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    @pre_dump
    def _verify_dump(self, data, **kwargs):
        # Declare required attributes
        self.dump_fields.update(
            headers=fields.Nested(HeadersSchema, attribute="headers", required=True),
            devices=fields.List(
                fields.Nested(DeviceDiscoverySchema, attribute="devices", required=True)
            ),
        )
        # Verify Authentication non-required attribute.
        if data.authentication:
            self.dump_fields.update(
                authentication=fields.Nested(
                    AuthenticationSchema, attribute="authentication"
                )
            )
        return data
