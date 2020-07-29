# TODO:
# CallbackAuthentication -> AccessTokenRequest Body
# Authentication -> authentication attribute to perform
# state and discovery callbacks.
import requests
from stschema.schema_callbacks.callbacks import (
    AccessTokenRequest,
    AccessTokenRequestSchema
)

class SchemaCallback:
    """
    The SchemaCallback class provides
    interface resources to interact
    with the ST Schema platform from
    an SchemaConnector instance (third-party cloud).

    This class covers:
        - Access Token Request.
        - Refresh token Request (TBD).
        - Device State Callback.
        - Device Discovery Callback.
    """
    @classmethod
    def access_token_request(cls, client_id:str, client_secret: str, code: str, request_id: str, url: str):
        """
        The access_token_request performs a
        POST Http Requests to the SmartThings
        platform to request an Authorization
        Token.
            :::param client_id (required)
            :::param client_secret (required)
            :::param code (required)
            :::param request_id (required)
            :::param url (required)
        """
        if not url.startswith('https://'):
            raise TypeError('"url" argument not valid, must be an "https://" Url.')
        else:
            return cls._access_token_request(
                client_id,
                client_secret,
                code,
                request_id,
                url
            )

    @staticmethod
    def _access_token_request(*auth_args):
        # Private method that will instance and
        # serialize an AccessTokenRequest object
        # as Request Body to ST Schema OAuth.
        #
        # AccessTokenRequest Instance.
        authentication_data = AccessTokenRequest(
            client_id=auth_args[0],
            client_secret=auth_args[1],
            code=auth_args[2],
            request_id=auth_args[3]
        )
        # Schema Instance and serialization steps,
        schema = AccessTokenRequestSchema()
        authentication_body = schema.dump(authentication_data)
        # POST Http Request to ST Schema
        # OAuth server.
        token_request = requests.post(
            url=auth_args[4],  # Url argument
            json=authentication_body
        )
        return token_request.json()

    def state_callback(self, request_id: str, devices: list, access_token: str):
        # WIP
        pass

    @staticmethod
    def _state_callback():
        # WIP
        pass

    def discovery_callback(self, request_id: str, devices: list, access_token: str):
        # WIP
        pass

    @staticmethod
    def _discovery_callback():
        # WIP
        pass
