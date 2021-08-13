# MIT License
#
# Copyright (c) 2021 Erick Israel Vazquez Neri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
class BaseDevice:
    """
    The BaseDevice class represents
    the basic metadata of a device
    integrations.
        :::param external_device_id
        :::param friendly_name
        :::param device_handler_type
        :::param device_cookie
        :::param unique_device_id
    """

    def __init__(
        self,
        external_device_id: str,
        friendly_name: str,
        device_unique_id: str,
        device_cookie: str,
        device_handler_type: str,
    ) -> "BaseDevice":
        self.external_device_id = external_device_id
        self.friendly_name = friendly_name
        self.device_unique_id = device_unique_id
        self.device_cookie = device_cookie
        self.device_handler_type = device_handler_type
