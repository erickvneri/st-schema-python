from marshmallow import Schema, fields
from stschema.interface.schemas import DeviceDiscoverySchema, DeviceStateSchema
from stschema.base.util import HeadersSchema


class ConnectorSchema(Schema):
    """The ConnectorSchema handles the
    serialization of the DiscoveryResponse
    and StateResponse classes.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions."""

    def __init__(self):
        Schema.__init__(self, unknown=True)

    headers = fields.Nested(HeadersSchema, attribute='headers', allow_none=False)
    devices = fields.List(fields.Nested(DeviceDiscoverySchema, attribute='devices', allow_none=True))
    deviceState = fields.List(fields.Nested(DeviceStateSchema), attribute='device_state', allow_none=True)
    commands = fields.List(fields.Field())
