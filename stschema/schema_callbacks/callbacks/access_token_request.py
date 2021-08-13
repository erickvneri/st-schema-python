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
    CallbackAuthentication,
    CallbackAuthSchema,
    HeadersSchema,
    BaseResponse,
)


class AccessTokenRequest(BaseResponse):
    """
    The AccessTokenRequest class handles the
    information necessary to request or refresh
    Access Tokens at the SmartThings Cloud.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        refresh_token: str,
        request_id: str,
        grant_type: str = "authorization_code",
    ) -> "AccessTokenRequest":
        BaseResponse.__init__(
            self, interaction_type="accessTokenRequest", request_id=request_id
        )

        # Refresh Token reference
        if not code and refresh_token:
            grant_type = "refresh_token"
            self.headers.interaction_type = "refreshAccessTokens"

        self.callback_authentication = CallbackAuthentication(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            refresh_token=refresh_token,
            grant_type=grant_type,
        )


class AccessTokenRequestSchema(Schema):
    """
    The AccessTokenRequestSchema handles the
    serialization of AccessTokenRequest
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    headers = fields.Nested(HeadersSchema, attribute="headers", required=True)
    callbackAuthentication = fields.Nested(
        CallbackAuthSchema, attribute="callback_authentication", required=True
    )
