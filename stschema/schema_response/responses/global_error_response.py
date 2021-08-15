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
from marshmallow import Schema, fields
from stschema.util.base_modules import (
    HeadersSchema,
    BaseResponse,
    BaseError,
    BaseErrorSchema,
)


class GlobalErrorResponse(BaseResponse):
    """
    The GlobalErrorResponse is an object
    representation of a global-contextual
    error.

        :::param interaction_type (required)
        :::param request_id (required)
        :::param global_error: BaseError instance.
    """

    def __init__(
        self, interaction_type: str, request_id: str, global_error: object
    ) -> "GlobalErrorResponse":
        BaseResponse.__init__(self, interaction_type, request_id)
        # BaseError instance
        self.global_error = global_error


class GlobalErrorSchema(Schema):
    """
    The GlobalErrorSchema handles
    the serialization of the
    GlobalErrorResponse classsupporting
    the nested BaseErrorSchema and
    HeadersSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    headers = fields.Nested(HeadersSchema, attribute="headers")
    globalError = fields.Nested(BaseErrorSchema, attribute="global_error")
