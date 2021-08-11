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


class ManufacturerInfo:
    """
    The ManufacturerInfo represents
    the device's metadata in context of
    a product.
        :::param manufacturer_name
        :::param model_name
        :::param hw_version
        :::param sw_version
    """

    def __init__(
        self, manufacturer_name: str, model_name: str, hw_version: str, sw_version: str
    ) -> "ManufacturerInfo":
        self.manufacturer_name = manufacturer_name
        self.model_name = model_name
        self.hw_version = hw_version
        self.sw_version = sw_version


class ManufacturerSchema(Schema):
    """
    The ManufacturerSchema handles the
    serialization of the ManufacturerInfo
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    manufacturerName = fields.Str(attribute="manufacturer_name", required=True)
    modelName = fields.Str(attribute="model_name", required=True)
    hwVersion = fields.Str(attribute="hw_version")
    swVersion = fields.Str(attribute="sw_version")
