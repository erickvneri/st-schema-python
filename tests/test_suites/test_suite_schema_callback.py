import pytest
from stschema.schema_callbacks import SchemaCallback


class TestSuiteSchemaCallbacks:
    """
    Test Suite on SchemaCallback Interface.

    Index:
        - TestSchemaCallbackAttributes
        - TestAccessTokenResource
        - TestStateCallback
        - TestDiscoveryCallback
    """
    class TestSchemaCallbackAttributes:
        def test_documentation(self):
            assert SchemaCallback
            assert SchemaCallback.__doc__

        def test_public_methods(self):
            assert SchemaCallback.access_token_request
            assert SchemaCallback.state_callback
            assert SchemaCallback.discovery_callback

        def test_private_methods(self):
            assert SchemaCallback._access_token_request
            assert SchemaCallback._state_callback
            assert SchemaCallback._discovery_callback


    class TestAccessTokenResource:
        # Test case on access_token_request
        # resource interface.
        def test_resource_documentation(self):
            assert SchemaCallback.access_token_request
            assert SchemaCallback.access_token_request.__doc__

        @pytest.mark.skip()
        def test_access_token_request(self):
            # Test case to check real-time HttpRequests,
            # unskip it and define Url below.
            custom_test_url=''
            assert SchemaCallback.access_token_request(
                'client_id',
                'client_secret',
                'code',
                'request_id',
                custom_test_url
            )

        def test_type_error_instances(self):
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request()
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request('client_id')
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request(
                    'client_id',
                    'client_secret'
                )
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request(
                    'client_id',
                    'client_secret',
                    'code'
                )
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request(
                    'client_id',
                    'client_secret',
                    'code',
                    'request_id'
                )
            # Wrong argument
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request(
                    'client_id',
                    'client_secret',
                    'code',
                    'request_id',
                    'url'
                )
