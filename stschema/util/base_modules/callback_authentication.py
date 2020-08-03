from marshmallow import Schema, fields


class CallbackAuthentication:
    """
    The CallbackAuthentication class
    represents the base information
    to authenticate the third-party cloud
    and perform the following interaction
    types:
        - Access Token Request.
        - State Callback.
        - Discovery Callback.
    """
    def __init__(self, client_id: str, client_secret: str, code: str, grant_type: str) -> 'CallbackAuthentication':
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.grant_type = grant_type


class CallbackAuthSchema(Schema):
    """
    The CallbackAuthSchema handles the
    serialization of CallbackAuthentication
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """
    clientId = fields.Str(attribute='client_id', required=True, dump_only=True)
    clientSecret = fields.Str(attribute='client_secret', required=True, dump_only=True)
    code = fields.Str(attribute='code', required=True, dump_only=True)
    grantType = fields.Str(attribute='grant_type', required=True, dump_only=True)
