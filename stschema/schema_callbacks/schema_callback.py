import json
from urllib import request
# SchemaDevice import for error handling
from stschema import SchemaDevice
# Schemas
from stschema.schema_response.responses import (
    StateRefreshResponseSchema,
    DiscoveryResponseSchema)
# Callback interaction type objects and schemas
from stschema.schema_callbacks.callbacks import (
    AccessTokenRequest,
    AccessTokenRequestSchema,
    StateCallback,
    DiscoveryCallback)

class SchemaCallback:
    """
    The SchemaCallback class provides
    interface resources to interact
    with the ST Schema platform from
    an SchemaConnector instance (third-party cloud).

    This class covers:
        - Access Token Request.
        - Refresh Access Tokens.
        - Device State Callback.
        - Device Discovery Callback.
    """
    @classmethod
    def access_token_request(cls, client_id:str, client_secret: str, code: str, refresh_token:str, request_id: str, url: str):
        """
        The access_token_request performs a
        POST Http Requests to the SmartThings
        platform to request or refresh
        Authorization Tokens.
            :::param client_id (required)
            :::param client_secret (required)
            :::param code (required)
            :::param refresh_token (required)
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
                refresh_token,
                request_id,
                url)

    @classmethod
    def _access_token_request(cls, *auth_args):
        # Private method that will instance and
        # serialize an AccessTokenRequest object
        # as Request Body to ST Schema OAuth.

        # AccessTokenRequest Instance.
        authentication_data = AccessTokenRequest(
            client_id=auth_args[0],
            client_secret=auth_args[1],
            code=auth_args[2],
            refresh_token=auth_args[3],
            request_id=auth_args[4])

        # Schema Instance and serialization steps.
        schema = AccessTokenRequestSchema()
        authentication_body = schema.dump(authentication_data)

        # POST Http Request to ST Schema
        # OAuth server.
        token_http_request = cls._http_request(
            url=auth_args[5],
            json_data=authentication_body)
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
        if not cls._validate_callback_args(url, devices):
            return cls._state_callback(
                access_token,
                request_id,
                url,
                devices)

    @classmethod
    def _state_callback(cls, *callback_args):
        # Private method that will instance and
        # serialize a StateCallback object as
        # Request Body to ST Schema cloud.

        # StateCallback Instance
        state_callback = StateCallback(
            callback_args[0],
            callback_args[1],
            callback_args[3])

        # Schema Instance and serialization steps.
        schema = StateRefreshResponseSchema()
        callback_request_body = schema.dump(state_callback)

        # Post Http Request to ST Schema
        # server.
        return cls._http_request(
            url=callback_args[2],
            json_data=callback_request_body)

    @classmethod
    def discovery_callback(cls, access_token: str, request_id: str, url: str, devices: list) -> object:
        """
        The discovery_callback performs a
        POST Http Requests to the SmartThings
        platform to push new SchemaDevice
        instances.
            :::param access_token (required)
            :::param request_id (required)
            :::param url (required)
            :::param devices (required)
        """
        if not cls._validate_callback_args(url, devices):
            return cls._discovery_callback(
                access_token,
                request_id,
                url,
                devices)

    @classmethod
    def _discovery_callback(cls, *callback_args):
        # Private method that will instance and
        # serialize a DiscoveryCallback object as
        # Request body to ST Schema Cloud.

        # DiscoveryCallback Instance.
        discovery_callback = DiscoveryCallback(
            access_token=callback_args[0],
            request_id=callback_args[1],
            devices=callback_args[3])

        # Schema Instance and serialization steps
        schema = DiscoveryResponseSchema()
        discovery_callback_body = schema.dump(discovery_callback)

        # POST Http Request to ST Schema
        # server.
        return cls._http_request(
            url=callback_args[2],
            json_data=discovery_callback_body)

    @staticmethod
    def _http_request(url: str, json_data: dict):
        # Private method that will
        # perform the Post Http Request.
        http_req = request.Request(url)
        http_req.add_header('Content-Type', 'application/json')

        return request.urlopen(
            http_req,
            json.dumps(json_data).encode('utf-8'))

    @staticmethod
    def _validate_callback_args(*callback_args) -> None:
        # Validate Url's protocol
        if not callback_args[0].startswith('https://'):
            raise TypeError('url argument not valid, must be Http Secure.')
        # Validate devices argument type
        if not isinstance(callback_args[1], list):
            raise TypeError('devices argument must be instance of list, not %s' % type(callback_args[1]))
        else:
            # Validate devices items instances
            for device in callback_args[1]:
                if not isinstance(device, SchemaDevice):
                    raise TypeError('devices items must be instance of %s, not %s', (SchemaDevice, type(callback_args[1])))
