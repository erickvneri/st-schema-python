import pytest
from hashlib import sha1
from pystschema import Header, HeadersSchema


class TestSTHeader:
    @pytest.fixture
    def def_header(self):
        req_id = sha1(b'requestID').hexdigest()
        header = Header(interaction_type='DiscoveryRequest', request_id=req_id)
        yield header

    @pytest.fixture
    def header_schema(self):
        header_schema = HeadersSchema()
        yield header_schema

    def test_header_class_construction(self):
        assert Header.__doc__
        assert len(Header.__doc__) != 0
    def test_header_schema_construction(self):
        assert HeadersSchema.__doc__
        assert len(HeadersSchema.__doc__) != 0

    def test_def_header(self, def_header):
        assert isinstance(def_header, Header)
        assert def_header.interaction_type == 'DiscoveryRequest'
        assert def_header.schema == 'st-schema'
        assert def_header.version == '1.0'
        assert def_header.request_id is not None

    def test_dumped_header(self, def_header, header_schema):
        result_header = header_schema.dump(def_header)

        assert type(result_header) is dict
        assert result_header['schema'] == 'st-schema'
        assert result_header['version'] == '1.0'
        assert result_header['interactionType'] == 'DiscoveryRequest'
        assert result_header['requestId'] is not None
