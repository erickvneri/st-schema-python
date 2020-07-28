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

    def __init__(self, manufacturer_name: str, model_name: str, hw_version: str, sw_version: str) -> 'ManufacturerInfo':
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

    manufacturerName = fields.Str(attribute='manufacturer_name', required=True)
    modelName = fields.Str(attribute='model_name', required=True)
    hwVersion = fields.Str(attribute='hw_version')
    swVersion = fields.Str(attribute='sw_version')
