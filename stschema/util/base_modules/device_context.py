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
from typing import List
from marshmallow import Schema, fields


class DeviceContext:
    """
    The DeviceContext represents the
    context/location metadata of the
    device integration.
        :::param room_name
        :::param groups
        :::param categories
    """

    def __init__(
        self, room_name: str, groups: List[str], categories: List[str]
    ) -> "DeviceContext":
        self.room_name = room_name
        self.groups = groups or list()
        self.categories = categories or list()


class DeviceContextSchema(Schema):
    """
    The DeviceContextSchema handles the
    serialization of the DeviceContext
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    roomName = fields.Str(attribute="room_name")
    groups = fields.List(fields.Str(attribute="groups"))
    categories = fields.List(fields.Str(attribute="categories"))
