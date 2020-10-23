from marshmallow import Schema, fields


class BaseAuthentication:
    """
    The BaseAuthentication class represents
    the attribute "authentication" that includes
    the Authorization Token needed to perform
    successful Calbacks into the SmartThings API.
    """
    def __init__(self, token: str, token_type: str='Bearer') -> 'BaseAuthentication':
        self.token = token
        self.token_type = token_type

class AuthenticationSchema(Schema):
    """
    The AuthenticationSchema handles the
    serialization of BaseAuthentication
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """
    token = fields.Str(required=True)
    tokenType = fields.Str(required=True, attribute='token_type')
