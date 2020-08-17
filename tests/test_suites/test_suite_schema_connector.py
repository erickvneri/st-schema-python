# Test Suite on SchemaConnector Interface Class
# which will test its construction and the
# instantiation flexibility triggering a few
# Exceptions to debug the SchemaConnector
# development
#
# The first test case handles the documentation
# and construction of the class, Private and
# Public methods along with the inherited
# methods.
#
# The second test case handles the flow-control
# of the main resource method that will give
# access to the interaction resource handlers:
#   -discovery_handler
#   -state_refresh_handler
#   -command_handler
#   -grant_callback_access
#   -integration_deleted
import pytest
from stschema import SchemaConnector


class TestSuiteSchemaConnector:
    """
    Test Suite on SchemaConnector interface class:

    Index:
        - TestCaseInterfaceClass
        - TestCaseInteractionHandlerMethod
    """
    class TestCaseInterfaceClass:
        # Test case on construction attributes
        # of the SchemaConnector interface class.
        def test_documentation(self):
            assert SchemaConnector.__doc__
            assert len(SchemaConnector.__doc__) > 0

        def test_public_methods(self):
            # Public methods from SchemaConnector
            assert SchemaConnector.interaction_handler
            assert SchemaConnector.discovery_handler
            assert SchemaConnector.state_refresh_handler
            assert SchemaConnector.command_handler
            assert SchemaConnector.grant_callback_access
            assert SchemaConnector.integration_deleted

        def test_private_methods(self):
            # Private methods from SchemaConnector
            assert SchemaConnector._interaction_handler

        def test_inherited_public_methods(self):
            # Public methods inherited
            # from SchemaResponse.
            assert SchemaConnector.discovery_response
            assert SchemaConnector.state_refresh_response
            assert SchemaConnector.command_response

        def test_inherited_private_methods(self):
            # Private methods inherited
            # from SchemaResponse.
            assert SchemaConnector._discovery_response
            assert SchemaConnector._state_refresh_response
            assert SchemaConnector._command_response
            assert SchemaConnector._validate_schema_response


    class TestCaseInteractionHandlerMethod:
        # Test case on method workflow:
        #   - intearction_handler
        def test_type_error_data_type_argument(self):
            sc = SchemaConnector()
            with pytest.raises(TypeError):
                sc.interaction_handler(json_data=str('STRING_ARGUMENT'))
            with pytest.raises(TypeError):
                sc.interaction_handler(json_data=int(123456))
            with pytest.raises(TypeError):
                sc.interaction_handler(json_data=set(123456))
            with pytest.raises(TypeError):
                sc.interaction_handler(json_data=tuple(123456))
            with pytest.raises(TypeError):
                sc.interaction_handler(json_data=list(123456))

        def test_attribute_error_missing_attributes(self):
            # Test that checks for Exceptions
            # raised when handler doesn't
            # receive critical attributes to
            # create successful responses.
            sc = SchemaConnector()
            with pytest.raises(AttributeError):
                sc.interaction_handler(dict(key='value'))
            with pytest.raises(AttributeError):
                sc.interaction_handler(dict(headers='value'))
            with pytest.raises(AttributeError):
                sc.interaction_handler(
                    dict(headers={
                        'requestId': 'xxxxx'
                }))
            with pytest.raises(AttributeError):
                sc.interaction_handler(
                    dict(headers={
                        'interactionType': 'xxxxx'
                    }))

        def test_not_implemented_handlers(self):
            # Test on Interaction Resource
            # handlers raising NotImplementedError
            # Exceptions as they're intended to be
            # implemented by substitution.
            sc = SchemaConnector()
            devices_arg = []
            headers_arg = dict(
                requestId='abcdefg',
                interactionType='discoveryRequest'
            )
            auth_args = dict(
                token='abc-123-xyz',
                tokenType='Bearer'
            )
            json_data_dict = dict(
                headers=headers_arg,
                authorization=auth_args,
                devices=devices_arg
            )
            with pytest.raises(NotImplementedError):
                sc.interaction_handler(json_data_dict)
            with pytest.raises(NotImplementedError):
                headers_arg['interactionType'] = 'stateRefreshRequest'
                sc.interaction_handler(json_data_dict)
            with pytest.raises(NotImplementedError):
                headers_arg['interactionType'] = 'commandRequest'
                sc.interaction_handler(json_data_dict)
            with pytest.raises(NotImplementedError):
                headers_arg['interactionType'] = 'grantCallbackAccess'
                json_data_dict['callbackAuthentication'] = 'xxxxx'
                json_data_dict['callbackUrls'] = 'xxxxx'
                sc.interaction_handler(json_data_dict)
            with pytest.raises(NotImplementedError):
                headers_arg['interactionType'] = 'integrationDeleted'
                sc.interaction_handler(json_data_dict)
            with pytest.raises(NotImplementedError):
                headers_arg['interactionType'] = 'interactionResult'
                sc.interaction_handler(json_data_dict)
