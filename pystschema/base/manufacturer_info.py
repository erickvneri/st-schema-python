from marshmallow import Schema, fields

class ManufacturerInfo:
    """The ManufacturerInfo class contains the
    information about the manufacturer company
    and the hardware and software versions
    of the device:

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
    It parses the Snake Cased attributes to a
    Camel Case format following REST conventions
    for Cloud-to-Cloud communication:

            :::param manufacturer_name -> manufacturerName
            :::param model_name -> modelName
            :::param hw_version -> hwVersion
            :::param sw_version -> swVersion"""

    manufacturerName = fields.Str(attribute='manufacturer_name', dump_only=True)
    modelName = fields.Str(attribute='model_name', dump_only=True)
    hwVersion = fields.Str(attribute='hw_version', dump_only=True)
    swVersion = fields.Str(attribute='sw_version', dump_only=True)