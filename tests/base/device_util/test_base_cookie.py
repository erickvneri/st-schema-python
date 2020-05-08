import pytest
from datetime import datetime
from stschema.base.device import BaseCookie, DeviceCookieSchema


class TestDeviceCookie(object):
    """This class will test the device cookie
    that will be used to track every update
    applied to the device."""

    @pytest.fixture
    def device_cookie(self):
        cookie_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cookie = BaseCookie(cookie=cookie_date)
        yield cookie

    @pytest.fixture
    def schema(self):
        schema = DeviceCookieSchema()
        yield schema

    def test_class_documentation(self):
        assert BaseCookie.__doc__
        assert len(BaseCookie.__doc__) != 0

    def test_schema_documentation(self):
        assert DeviceCookieSchema.__doc__
        assert len(DeviceCookieSchema.__doc__) != 0

    def test_device_cookie_instance(self, device_cookie):
        assert device_cookie
        assert device_cookie.cookie
        assert isinstance(device_cookie, BaseCookie)
        assert type(device_cookie.cookie) is str
        assert device_cookie.cookie == datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def test_device_cookie_schema_instance(self, device_cookie, schema):
        dumped_cookie = schema.dump(device_cookie)
        assert dumped_cookie
        assert dumped_cookie['cookie']
        assert dumped_cookie['cookie'] == device_cookie.cookie

    def test_device_cookie_schema_composition(self, schema):
        assert schema
        assert schema.fields['cookie']

    def test_device_cookie_class_extra_values(self):
        with pytest.raises(TypeError):
            multiple_cookies = BaseCookie(cookie='cookie_1', cookie_2='last_year_cookie')
            assert multiple_cookies
            assert multiple_cookies.cookie
            assert isinstance(multiple_cookies, BaseCookie)
            assert type(multiple_cookies.cookie) is str
            assert multiple_cookies.cookie == 'cookie_1'

    def test_device_cookie_class_none_values(self):
        with pytest.raises(TypeError):
            cookie = BaseCookie()
