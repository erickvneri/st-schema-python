from stschema.base.response import BaseResponse, BaseHeaders
import hashlib
import pytest


class TestBaseResponse(object):
    """This test will validate that the
    BaseResponse class serves properly the
    main attributes of the main interaction
    types:
        :::headers
        :::devices
        :::device_state"""

    @pytest.fixture
    def res_instance(self):
        req_id = hashlib.sha1(b'requestId').hexdigest()
        interaction_type = 'discoveryTest'
        instance = BaseResponse(interaction_type=interaction_type, request_id=req_id)
        yield instance

    def test_class_documentation(self, res_instance):
        assert res_instance
        assert res_instance.__doc__
        assert len(res_instance.__doc__) != 0

    def test_base_response_instance_attrs(self, res_instance):
        assert res_instance
        assert res_instance.headers
        assert isinstance(res_instance, BaseResponse)
        assert type(res_instance.devices) is list
        assert type(res_instance.device_state) is list

    def test_base_response_headers_composition(self, res_instance):
        assert res_instance.headers
        assert isinstance(res_instance.headers, BaseHeaders)
        assert res_instance.headers.schema
        assert res_instance.headers.version
        assert res_instance.headers.request_id
        assert res_instance.headers.interaction_type

    def test_type_error_instance_null_values(self):
        with pytest.raises(TypeError):
            BaseResponse()

    def test_type_error_instance_extra_value(self):
        with pytest.raises(TypeError):
            BaseResponse(
                interaction_type='interactionType',
                request_id=hashlib.sha1(b'requestId').hexdigest(),
                extra=0
            )
