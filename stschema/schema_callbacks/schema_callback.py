import requests
from stschema import SchemaDevice
from stschema.schema_response.responses import StateRefreshResponseSchema
from stschema.schema_callbacks.callbacks import (
    AccessTokenRequest,
    AccessTokenRequestSchema,
    StateCallback
)

class SchemaCallback:
    """
    The SchemaCallback class provides
    interface resources to interact
    with the ST Schema platform from
    an SchemaConnector instance (third-party cloud).

    This class covers:
        - Access Token Request.
        - Refresh Token Request (TBD).
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
            raise TypeError('"url" argument not valid, must be Http Secure.')
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
        # Schema Instance and serialization steps.
        schema = AccessTokenRequestSchema()
        authentication_body = schema.dump(authentication_data)
        # POST Http Request to ST Schema
        # OAuth server.
        token_http_request = requests.post(
            url=auth_args[4],  # Url argument
            json=authentication_body
        )
        return token_http_request

    @classmethod
    def state_callback(cls, access_token: str, request_id: str, url: str, devices: list) -> object:
        """
        The state_callback performs a
        POST Http Requests to the SmartThings
        platform to push a new state to the
        devices passed
            :::param access_token (required)
            :::param request_id (required)
            :::param url (required)
            :::param devices (required)
        """
        if not url.startswith('https://'):
            raise TypeError('url argument not valid, must be Http Secure.')
        if not isinstance(devices, list):
            raise TypeError('devices argument must be instance of list, not %s' % type(devices))
        else:
            for device in devices:
                if not isinstance(device, SchemaDevice):
                    raise TypeError('devices items must be instance of %s, not %s', (SchemaDevice, type(device)))
        return cls._state_callback(
            access_token,
            request_id,
            url,
            devices
        )

    @staticmethod
    def _state_callback(*callback_args):
        # Private method that will instance and
        # serialize a StateCallback object as
        # Request Body to ST Schema cloud.
        #
        # StateCallback Instance
        state_callback = StateCallback(
            callback_args[0],
            callback_args[1],
            callback_args[3]
        )
        # Schema Instance and serialization steps.
        schema = StateRefreshResponseSchema()
        state_callback_body = schema.dump(state_callback)
        # Post Http Request to ST Schema
        state_http_callback = requests.post(
            url=callback_args[2],
            json=state_callback_body
        )
        return state_http_callback

    def discovery_callback(self, request_id: str, devices: list, access_token: str):
        # WIP
        pass

    @staticmethod
    def _discovery_callback():
        # WIP
        pass
