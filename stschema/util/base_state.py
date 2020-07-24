from marshmallow import Schema, fields


class BaseState:
    """The BaseState uses the capability's
    metadata to represent a device's state.
        :::param component
        :::param capability
        :::param attribute
        :::param value

    For more information about the supported
    capabilities read te Capabilities Reference:
    - https://smartthings.developer.samsung.com/docs/api-ref/capabilities.html"""

    def __init__(self, capability: str, attribute: str, value, unit: str, component: str) -> 'BaseState':
        self.component = component
        self.capability = capability
        self.attribute = attribute
        self.value = value
        if unit:
            self.unit = unit


class StateSchema(Schema):
    """The StateSchema handles the
    serialization of the BaseState
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects."""

    component = fields.Str()
    capability = fields.Str()
    attribute = fields.Str()
    value = fields.Field()
    unit = fields.Str()
