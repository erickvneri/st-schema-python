# The SchemaConnector class provides a json_data
# handler that will take the entity-body of a
# Webhook Http Request and process it according to
# the Interaction Type passed. It is intended to be
# used with JSON data only.
#
# Also, it provides a series of Interaction Type
# handler interfaces that will parse the JSON body
# and pass the necessary information to simplify
# the development of Schema Connector instances.
import logging
from stschema.schema_response import SchemaResponse


class SchemaConnector(SchemaResponse):
    """
    The Schema Connector class provides
    a developer interface to control the flow
    of Interaction Types through interaction
    resource handlers.
        :::param enable_logger: boolean (WIP) # TODO: Create logger instance
    """
    def __init__(self, enable_logger: bool=False):
        pass

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
            # Collectiong SmartThings Schema Headers
            # information that contains critical
            # information:
            #   - Request Id
            #   - Interaction Types.
            headers_args = json_data.get('headers')
            if not headers_args:
                raise AttributeError('missing "headers" attribute at json_data')
            else:
                request_id_arg = headers_args.get('requestId')
                interaction_type_arg = headers_args.get('interactionType')
                if not request_id_arg:
                    raise AttributeError('missing "requestId" attribute at json_data.headers')
                elif not interaction_type_arg:
                    raise AttributeError('missing "interactionType" attribute at json_data.headers')
                else:
                    return self._interaction_handler(json_data)

    def _interaction_handler(self, data):
        data_headers = data['headers']
        interaction_type = data_headers['interactionType']
        request_id = data_headers['requestId']
        # Handle interaction type
        if interaction_type == 'discoveryRequest':
            return self.discovery_handler(request_id)
        elif interaction_type == 'stateRefreshRequest':
            return self.state_refresh_handler(data['devices'], request_id)
        elif interaction_type == 'commandRequest':
            return self.command_handler(data['devices'], request_id)
        elif interaction_type == 'grantCallbackAccess':
            return self.grant_callback_access(data['callbackAuthentication'])
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

    def discovery_handler(self, request_id: str):
        raise NotImplementedError('Interaction resource handler not implemented')

    def state_refresh_handler(self, devices: list, request_id: str):
        raise NotImplementedError('Interaction resource handler not implemented')

    def command_handler(self, devices: list, request_id: str):
        raise NotImplementedError('Interaction resource handler not implemented')

    def grant_callback_access(self, callback_authentication: dict):
        raise NotImplementedError('Interaction resource handler not implemented')

    def integration_deleted(self, callback_authentication: dict):
        raise NotImplementedError('Interaction resource handler not implemented')

    def interaction_result_handler(self, interaction_result: dict, origin: str):
        raise NotImplementedError('Interaction resource handler not implemented')
