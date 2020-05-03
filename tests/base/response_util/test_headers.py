import pytest
from hashlib import sha1
from stschema.responses.util import Header, HeadersSchema


class TestResponseHeader(object):
    """This test will be applied to the
    Header class, which is used  at every
    interaction type response."""

    @pytest.fixture
    def def_header(self):
        req_id = sha1(b'requestID').hexdigest()
        header = Header(interaction_type='interactionType', request_id=req_id)
        yield header

    @pytest.fixture
    def header_schema(self):
        header_schema = HeadersSchema()
        yield header_schema

    def test_header_class_documentation(self):
        assert Header.__doc__
        assert len(Header.__doc__) != 0

    def test_header_schema_documentation(self):
        assert HeadersSchema.__doc__
        assert len(HeadersSchema.__doc__) != 0

    def test_header_instance(self, def_header):
        assert isinstance(def_header, Header)
        assert def_header.interaction_type
        assert def_header.schema
        assert def_header.version
        assert def_header.request_id

    def test_header_schema_instance(self, def_header, header_schema):
        result_header = header_schema.dump(def_header)
        assert type(result_header) is dict
        assert result_header['schema']
        assert result_header['version']
        assert result_header['interactionType']
        assert result_header['requestId']

    def test_header_schema_composition(self, header_schema):
        assert header_schema
        assert header_schema.fields['schema']
        assert header_schema.fields['version']
        assert header_schema.fields['interactionType']
        assert header_schema.fields['requestId']

    def test_type_error_instance_null_values(self):
        with pytest.raises(TypeError):
            header = Header()

    def test_type_error_instance_extra_value(self):
        with pytest.raises(TypeError):
            header = Header(interaction_type='interaction_type', request_id='request_id_hash', extra=0)
