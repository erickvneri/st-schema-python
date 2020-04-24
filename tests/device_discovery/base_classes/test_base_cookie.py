import pytest
from datetime import datetime
from pystschema.base import BaseCookie, DeviceCookieSchema

class TestDeviceCookie:
    @pytest.fixture
    def device_cookie(self):
        yield BaseCookie

    @pytest.fixture
    def schema(self):
        schema = DeviceCookieSchema()
        yield schema

    def test_class_construction(self):
        assert BaseCookie.__doc__
        assert len(BaseCookie.__doc__) != 0

    def test_schema_construction(self):
        assert DeviceCookieSchema.__doc__
        assert len(DeviceCookieSchema.__doc__) != 0

    def test_raw_cookie_definition(self, device_cookie):
        d_cookie = device_cookie(cookie='some_cookie')
        assert d_cookie
        assert d_cookie.cookie
        assert isinstance(d_cookie, BaseCookie)
        assert type(d_cookie.cookie) is str
        assert d_cookie.cookie == 'some_cookie'

    def test_multiple_values(self,  device_cookie):
        with pytest.raises(TypeError):
            multiple_cookies = device_cookie(cookie='cookie_1', cookie_2='last_year_cookie')
            assert multiple_cookies
            assert multiple_cookies.cookie
            assert isinstance(multiple_cookies, BaseCookie)
            assert type(multiple_cookies.cookie) is str
            assert multiple_cookies.cookie == 'cookie_1'

    def test_device_cookie_schema(self, device_cookie, schema):
        cookie_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cookie = device_cookie(cookie=cookie_date)
        dumped_cookie = schema.dump(cookie)
        assert dumped_cookie
        assert dumped_cookie['cookie']
        assert dumped_cookie['cookie'] == cookie.cookie
