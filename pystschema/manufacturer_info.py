from marshmallow import Schema, fields

class ManufacturerInfo:
    """The ManufacturerInfo class is used
    at the initial DiscoveryRequest. It
    contains the information about the
    manufacturer and the hardware and software
    versions of the device:

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
    """The ManufacturerSchema class will handle the
    serialization of the ManufacturerInfo class.
    It parses the snake cased attributes into Camel
    Case attributes as the ST-Schema documentation
    refers:

            :::param manufacturer_name -> manufacturerName
            :::param model_name -> modelName
            :::param hw_version -> hwVersion
            :::param sw_version -> swVersion"""

    manufacturerName = fields.Field(attribute='manufacturer_name')
    modelName = fields.Field(attribute='model_name')
    hwVersion = fields.Field(attribute='hw_version')
    swVersion = fields.Field(attribute='sw_version')