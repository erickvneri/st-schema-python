from marshmallow import Schema, fields
from stschema.util import (
    CallbackAuthentication,
    CallbackAuthSchema,
    HeadersSchema,
    BaseResponse
)


class AccessTokenRequest(BaseResponse):
    """
    The AccessTokenRequest class handles the
    information necessary to request Authorization
    tokens at the SmartThings Cloud.
    """
    def __init__(self,
        client_id: str,
        client_secret: str,
        code: str,
        request_id: str,
        grant_type: str='authorization_code') -> 'AccessTokenRequest':
        BaseResponse.__init__(self, interaction_type='accessTokenRequest', request_id=request_id)  # BaseResponse instance
        self.callback_authentication = CallbackAuthentication(  # CallbackAuthentication instance
            client_id = client_id,
            client_secret = client_secret,
            code = code,
            grant_type = grant_type
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
    headers = fields.Nested(HeadersSchema, attribute='headers', required=True)
    callbackAuthentication = fields.Nested(CallbackAuthSchema, attribute='callback_authentication', required=True)
