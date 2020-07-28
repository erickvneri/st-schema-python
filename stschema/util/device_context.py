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

    def __init__(self, room_name: str, groups: List[str], categories: List[str]) -> 'DeviceContext':
        self.room_name = room_name
        self.groups = groups or list()
        self.categories = categories or list()


class DeviceContextSchema(Schema):
    """
    The DeviceContextSchema handles the
    serialization of the DeviceContext class
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    roomName = fields.Str(attribute='room_name')
    groups = fields.List(fields.Str(attribute='groups'))
    categories = fields.List(fields.Str(attribute='categories'))
