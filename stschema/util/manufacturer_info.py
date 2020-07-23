from marshmallow import Schema, fields


class ManufacturerInfo:
    """The ManufacturerInfo class handles the
    device's information about its manufacture.
        :::param manufacturer_name: Company manufacturer
        :::param model_name: Commercial name of the device
        :::param hw_version: Hardware version
        :::param sw_version: Software version"""

    def __init__(self, manufacturer_name: str, model_name: str, hw_version: str, sw_version: str):
        self.manufacturer_name = manufacturer_name
        self.model_name = model_name
        self.hw_version = hw_version
        self.sw_version = sw_version


class ManufacturerSchema(Schema):
    """The ManufacturerSchema handles the
    serialization of the ManufacturerInfo class.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions.
            :::param manufacturer_name -> manufacturerName
            :::param model_name -> modelName
            :::param hw_version -> hwVersion
            :::param sw_version -> swVersion"""

    manufacturerName = fields.Str(attribute='manufacturer_name')
    modelName = fields.Str(attribute='model_name')
    hwVersion = fields.Str(attribute='hw_version')
    swVersion = fields.Str(attribute='sw_version')
