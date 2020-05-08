from typing import List
from marshmallow import Schema, fields


class DeviceContext:
    """The DeviceContext class contains the information
    about the device that refers to its utility or
    location of use.

        :::param room_name: dictate at which room
        the device will be assigned at the One App.
        :::param groups: group of devices that conforms
        the environment of the device.
        :::param categories: classifiers of the type of
        device (light, thermostats, monitoring, etc.)."""

    def __init__(self, room_name: str, groups: List[str] = None, categories: List[str] = None):
        self.room_name = room_name
        self.groups = groups or list()
        self.categories = categories or list()


class DeviceContextSchema(Schema):
    """The DeviceContextSchema handles the
    serialization of the DeviceContext class.
    It parses the Snake Cased attributes to a
    Camel Case format following REST conventions
    for Cloud-to-Cloud communication:

        :::param room_name -> roomName
        :::param groups
        :::param categories"""

    roomName = fields.Str(attribute='room_name')
    groups = fields.List(fields.Str(attribute='groups'))
    categories = fields.List(fields.Str(attribute='categories'))
