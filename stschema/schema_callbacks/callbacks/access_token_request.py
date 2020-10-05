from marshmallow import Schema, fields
from stschema.util.base_modules import (
    CallbackAuthentication,
    CallbackAuthSchema,
    HeadersSchema,
    BaseResponse
)


class AccessTokenRequest(BaseResponse):
    """
    The AccessTokenRequest class handles the
    information necessary to request or refresh
    Access Tokens at the SmartThings Cloud.
    """
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 code: str,
                 refresh_token: str,
                 request_id: str,
                 grant_type: str='authorization_code') -> 'AccessTokenRequest':
        BaseResponse.__init__(self, interaction_type='accessTokenRequest', request_id=request_id)

        # Refresh Token reference
        if not code and refresh_token:
            grant_type = 'refresh_token'
            self.headers.interaction_type = 'refreshAccessTokens'

        self.callback_authentication = CallbackAuthentication(
            client_id = client_id,
            client_secret = client_secret,
            code = code,
            refresh_token = refresh_token,
            grant_type = grant_type)


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
    headers = fields.Nested(HeadersSchema, attribute='headers', required=True)
    callbackAuthentication = fields.Nested(CallbackAuthSchema, attribute='callback_authentication', required=True)
