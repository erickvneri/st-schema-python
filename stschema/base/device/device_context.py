from typing import List
from marshmallow import Schema, fields


class DeviceContext(object):
    """The DeviceContext class handles the
    device's information about its default
    utility context.
        :::param room_name
        :::param groups
        :::param categories"""

    def __init__(self, room_name: str, groups: List[str], categories: List[str]):
        self.room_name = room_name
        self.groups = groups or list()
        self.categories = categories or list()


class DeviceContextSchema(Schema):
    """The DeviceContextSchema handles the
    serialization of the DeviceContext class.
    It converts Snake Case attributes to
    Camel Case format following the REST
    conventions.
        :::param room_name -> roomName
        :::param groups
        :::param categories"""

    roomName = fields.Str(attribute='room_name')
    groups = fields.List(fields.Str(attribute='groups'))
    categories = fields.List(fields.Str(attribute='categories'))
