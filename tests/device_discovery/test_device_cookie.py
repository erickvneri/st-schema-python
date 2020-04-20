import pytest
from pystschema import DeviceCookie, DeviceCookieSchema

class TestDeviceCookie:
    @pytest.fixture
    def device_cookie(self):
        yield DeviceCookie

    @pytest.fixture
    def schema(self):
        schema = DeviceCookieSchema()
        yield schema

    def test_raw_cookie_definition(self, device_cookie):
        raw_cookie = device_cookie(cookie='raw_definition')

        assert raw_cookie
        assert raw_cookie.cookie
        assert isinstance(raw_cookie, DeviceCookie)
        assert type(raw_cookie.cookie) is str
        assert raw_cookie.cookie == 'raw_definition'

    def test_issue_hashed_cookie(self, device_cookie):
        hashed_cookie = device_cookie.issue()

        assert hashed_cookie
        assert isinstance(hashed_cookie, DeviceCookie)
        assert type(hashed_cookie.cookie) is str

    def test_device_cookie_schema(self, device_cookie, schema):
        cookie = device_cookie.issue()
        dumped_cookie = schema.dump(cookie)

        assert dumped_cookie
        assert dumped_cookie['cookie']
        assert dumped_cookie['cookie'] == cookie.cookie
