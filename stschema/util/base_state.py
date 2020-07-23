from marshmallow import Schema, fields


class BaseState:
    """The BaseState class is the basic representation
    of the state of the device in reference to the
    capabilities attributed.
        :::param component
        :::param capability
        :::param attribute
        :::param value

    For more information about the supported
    capabilities read te Capabilities Reference:
    - https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html"""

    def __init__(self, capability: str, attribute: str, value, unit: str, component: str):
        self.component = component
        self.capability = capability
        self.attribute = attribute
        self.value = value
        if unit:
            self.unit = unit


class StateSchema(Schema):
    """The StateSchema class handles the
    serialization of the BaseState class."""

    component = fields.Str()
    capability = fields.Str()
    attribute = fields.Str()
    value = fields.Field()
    unit = fields.Str()