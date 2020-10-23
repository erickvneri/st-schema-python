from marshmallow import Schema, fields, pre_dump


class CallbackAuthentication:
    """
    The CallbackAuthentication class
    represents the base information
    to authenticate the third-party cloud
    and perform the following interaction
    types:
        - Access Token Request.
        - Refresh Access Tokens.
        - State Callback.
        - Discovery Callback.
    """
    def __init__(self, client_id: str, client_secret: str, code: str, refresh_token: str, grant_type: str) -> 'CallbackAuthentication':
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.refresh_token = refresh_token
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

    @pre_dump
    def _verify_dump(self, data, **kwargs):
        self.dump_fields.update(
            clientId = fields.Str(attribute='client_id', required=True, dump_only=True),
            clientSecret = fields.Str(attribute='client_secret', required=True, dump_only=True),
            grantType = fields.Str(attribute='grant_type', required=True, dump_only=True))
        if data.code:
            self.dump_fields.update(
                code = fields.Str(attribute='code', required=True, dump_only=True))
        elif data.refresh_token:
            self.dump_fields.update(
                refreshToken = fields.Str(attribute='refresh_token', required=True, dump_only=True))
        return data

