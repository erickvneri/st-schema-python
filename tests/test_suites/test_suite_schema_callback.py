import pytest
from stschema.schema_callbacks import SchemaCallback
from tests.device_fixture import SchemaDeviceFixture

# Url for testing Callbacks
custom_test_url = ''

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

        @pytest.mark.skip('COMMENT THIS LINE TO ENABLE TEST CASE')
        def test_access_token_request(self):
            # Test case to check real-time HttpRequests,
            # unskip to enable.
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

        def test_type_error_url(self):
            with pytest.raises(TypeError):
                assert SchemaCallback.access_token_request(
                        'client_id',
                        'client_secret',
                        'code',
                        'request_id',
                        'url'
                    )


    class TestStateCallbackMethod:
        # Test case on SchemaCallback.state_callback
        def test_documentation(self):
            assert SchemaCallback.state_callback
            assert SchemaCallback.state_callback.__doc__

        @pytest.mark.skip('COMMENT THIS LINE TO ENABLE TEST CASE')
        def test_state_callback(self):
            # Test case to check real-time HttpRequests,
            # unskip to enable.
            assert SchemaCallback.state_callback(
                'access_token',
                'request_id',
                custom_test_url,
                [SchemaDeviceFixture()]
            )

        def test_type_error_missing_arguments(self):
            with pytest.raises(TypeError):
                assert SchemaCallback.state_callback()
            with pytest.raises(TypeError):
                assert SchemaCallback.state_callback('access_token')
            with pytest.raises(TypeError):
                assert SchemaCallback.state_callback(
                    'access_token',
                    'request_id'
                )
            with pytest.raises(TypeError):
                assert SchemaCallback.state_callback(
                    'access_token',
                    'request_id',
                    'url'
                )

        def test_type_error_invalid_url(self):
            with pytest.raises(TypeError):
                assert SchemaCallback.state_callback(
                    'access_token',
                    'request_id',
                    'http://INVALID_URL',
                    []
                )

        def test_type_error_devices_argument(self):
            # TODO: Review for fixture update
            # Partial Fixture to test SchemaDevice
            # types inputs on responses.
            devices_argument = lambda data_type: \
                SchemaCallback.state_callback(
                    'access_token',
                    'request_id',
                    'https://TEST_URL_ARG',
                    data_type
                )
            with pytest.raises(TypeError):
                assert devices_argument(str('INVALID'))
            with pytest.raises(TypeError):
                assert devices_argument(int(10101010))
            with pytest.raises(TypeError):
                assert devices_argument(tuple(('INVALID')))
            with pytest.raises(TypeError):
                assert devices_argument(dict(key='val'))
            with pytest.raises(TypeError):
                assert devices_argument(bytes(b'1010101'))
            with pytest.raises(TypeError):
                assert devices_argument(frozenset({'INVALID'}))
            with pytest.raises(TypeError):
                assert devices_argument(set({'INVALID'}))

        def test_type_error_devices_arg_items(self):
            # TODO: Review for fixture update
            # Partial Fixture to test SchemaDevice
            # types inputs on responses.
            devices_argument = lambda data_type: \
                SchemaCallback.state_callback(
                    'access_token',
                    'request_id',
                    'https://TEST_URL_ARG',
                    data_type
                )
            with pytest.raises(TypeError):
                assert devices_argument([str('INVALID')])
            with pytest.raises(TypeError):
                assert devices_argument([int(10101010)])
            with pytest.raises(TypeError):
                assert devices_argument([tuple(('INVALID'))])
            with pytest.raises(TypeError):
                assert devices_argument([dict(key='val')])
            with pytest.raises(TypeError):
                assert devices_argument([bytes(b'1010101')])
            with pytest.raises(TypeError):
                assert devices_argument([frozenset({'INVALID'})])
            with pytest.raises(TypeError):
                assert devices_argument([set({'INVALID'})])
