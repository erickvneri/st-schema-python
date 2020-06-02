from stschema.base.util import ErrorEnum
from marshmallow import Schema, fields


class DeviceError(object):
    """The DeviceError class is the basic representation
    of the error state attributed to a single device.
        :::param error_enum
        :::param detail

        For more information about the supported
    error enums, read te ErrorResponses documentation:
    - https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/smartthings-schema-reference.html#Error-Responses"""

    def __init__(self, error_enum: ErrorEnum, detail: str):
        self.error_enum = ErrorEnum(error_enum)
        self.detail = detail


class DeviceErrorSchema(Schema):
    """The DeviceErrorSchema handles the
        serialization of the DeviceError class.
        It converts Snake Case attributes to
        Camel Case format following the REST
        conventions.
            :::param error_enum -> errorEnum
            :::param detail"""

    errorEnum = fields.Str(attribute='error_enum')
    detail = fields.Str()
