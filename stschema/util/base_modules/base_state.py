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
from marshmallow import Schema, fields


class BaseState:
    """
    The BaseState uses the capability's
    metadata to represent a device's state.
        :::param component
        :::param capability
        :::param attribute
        :::param value
        :::param unit
    """

    def __init__(
        self, capability: str, attribute: str, value, unit: str, component: str
    ) -> "BaseState":
        self.component = component
        self.capability = capability
        self.attribute = attribute
        self.value = value
        if unit:
            self.unit = unit


class StateSchema(Schema):
    """
    The StateSchema handles the
    serialization of the BaseState
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    component = fields.Str()
    capability = fields.Str()
    attribute = fields.Str()
    value = fields.Field()
    unit = fields.Str()
