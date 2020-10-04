"""
The SchemaConnector class provides a json_data
handler that will take the entity-body of a
Webhook Http Request and process it according to
the Interaction Type passed. It is intended to be
used with JSON data only.

Also, it provides a series of Interaction Type
handler interfaces that will parse the JSON body
and pass the necessary information to simplify
the development of Schema Connector instances.
"""
from stschema.schema_response import SchemaResponse
from stschema.util import EventLogger, ErrorHandler


class SchemaConnector(SchemaResponse):
    """
    The Schema Connector class provides
    a developer interface to control the flow
    of Interaction Types through interaction
    resource handlers.
        :::param enable_logger: boolean
    """
    def __init__(self, enable_logger: bool=False):
        self.logger = EventLogger(enable_logger).logger
        self.error_handler = ErrorHandler()

    def interaction_handler(self, json_data: dict):
        """
        This method helps with the
        flow-control of Interaction Types
        and returns interaction resource
        handlers respectively.
            :::param json_data: dict
        """

        if not isinstance(json_data, dict):
            raise TypeError('dict argument expected, not (%s, %s)' % (type(json_data), json_data))
        else:
            # Validating SmartThings Schema Headers
            # information that contains critical
            # values of requests persinstence.
            #   - Request Id
            #   - Interaction Type reference.
            headers_args = json_data.get('headers')
            # Validating authorization attribute
            # that contains the access token issued
            # by the OAuth2.0 server.
            auth_args = json_data.get('authentication')
            if not headers_args:
                raise AttributeError('missing or null "headers" attribute at json_data')
            elif not auth_args:
                raise AttributeError('missing or null "authentication" attribute at json_data')
            else:
                request_id_arg = headers_args.get('requestId')
                interaction_type_arg = headers_args.get('interactionType')
                if not request_id_arg:
                    raise AttributeError('missing or null "requestId" attribute at json_data.headers')
                elif not interaction_type_arg:
                    raise AttributeError('missing or null "interactionType" attribute at json_data.headers')
                else:
                    # Logging respective json_data
                    self.logger.info('[%s] - %s' % (interaction_type_arg, json_data))
                    return self._interaction_handler(json_data)

    def _interaction_handler(self, data):
        data_headers = data['headers']
        interaction_type = data_headers['interactionType']
        request_id = data_headers['requestId']
        access_token = data['authentication']['token']
        # Handle interaction type
        if interaction_type == 'discoveryRequest':
            return self.discovery_handler(request_id, access_token)
        elif interaction_type == 'stateRefreshRequest':
            return self.state_refresh_handler(data['devices'], request_id, access_token)
        elif interaction_type == 'commandRequest':
            return self.command_handler(data['devices'], request_id, access_token)
        elif interaction_type == 'grantCallbackAccess':
            return self.grant_callback_access(data['callbackAuthentication'], data['callbackUrls'])
        elif interaction_type == 'integrationDeleted':
            return self.integration_deleted(data['callbackAuthentication'])
        elif interaction_type == 'interactionResult':
            # Since detail of Interaction Types
            # are dynamic, instead of complex
            # flow-control conditions, headers
            # and authentication will be poped
            # before calling handler.
            if data.get('authentication'):
                data.pop('authentication')
            data.pop('headers')
            # Originating Interaction Type
            origin = data.get('originatingInteractionType')
            return self.interaction_result_handler(data, origin)

    def discovery_handler(self, request_id: str, access_token: str):
        """
        Implementation example handling
        specific attributes from json_data:

            discovery_handler(self, request_id, access_token):
                # Custom implementation here...
                return super().discovery_response(devices, request_id)
            ...
        """
        return self.error_handler.not_implemented_error('discovery_handler')

    def state_refresh_handler(self, devices: list, request_id: str, access_token: str):
        """
        Implementation example handling
        specific attributes from json_data:

            state_refresh_handler(self, devices, request_id, access_token):
                # Custom implementation here...
                return super().state_refresh_response(devices, request_id)
        """
        return self.error_handler.not_implemented_error('state_refresh_handler')

    def command_handler(self, devices: list, request_id: str, access_token: str):
        """
        Implementation example handling
        specific attributes from json_data:

            command_handler(self, devices, request_id, access_token):
                # Custom implementation here...
                return super().command_request(devices, request_id)
        """
        return self.error_handler.not_implemented_error('command_handler')

    def grant_callback_access(self, callback_authentication: dict, callback_urls: dict):
        """
        Implementation example handling
        specific attributes from json_data:

            grant_callback_access(self, callback_authentication):
            ...
        """
        return self.error_handler.not_implemented_error('grant_callback_access')

    def integration_deleted(self, callback_authentication: dict):
        """
        Implementation example handling
        specific attributes from json_data:

            integration_deleted(self, callback_authentication):
            ...
        """
        return self.error_handler.not_implemented_error('integration_deleted')

    def interaction_result_handler(self, interaction_result: dict, origin: str):
        """
        Implementation example handling
        specific attributes from json_data:

            interaction_result_handler(self, devices, request_id):
            ...
        """
        return self.error_handler.not_implemented_error('interaction_result_handler')
