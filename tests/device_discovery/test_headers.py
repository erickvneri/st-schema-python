import pytest
from hashlib import sha1
from pystschema import Header, HeadersSchema

@pytest.fixture
def def_header():
    yield Header

@pytest.fixture
def header_schema():
    header_schema = HeadersSchema()
    yield header_schema


def test_def_header(def_header):
    req_id = sha1(b'requestID').hexdigest()
    header = def_header(interaction_type='DiscoveryRequest', request_id=req_id)

    assert isinstance(header, Header)
    assert header.interaction_type == 'DiscoveryRequest'
    assert header.schema == 'st-schema'
    assert header.version == '1.0'
    assert header.request_id is not None

def test_dumped_header(def_header, header_schema):
    req_id = sha1(b'requestID').hexdigest()
    header = def_header(interaction_type='DiscoveryRequest', request_id=req_id)
    result_header = header_schema.dump(header)

    assert type(result_header) is dict
    assert result_header['interaction_type'] == 'DiscoveryRequest'
    assert result_header['schema'] == 'st-schema'
    assert result_header['version'] == '1.0'
    assert result_header['request_id'] is not None
