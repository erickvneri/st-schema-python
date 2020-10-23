from marshmallow import Schema, fields


class BaseError:
    """
    The BaseError class represents
    an error state definition. Used as
    a DeviceError or Global Error
    instance.
        :::param error_enum
        :::param detail
    """

    def __init__(self, error_enum: str, detail: str) -> 'BaseError':
        self.error_enum = error_enum
        self.detail = detail

class BaseErrorSchema(Schema):
    """
    The BaseError handles the
    serialization of the DeviceError
    class.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """

    errorEnum = fields.Str(attribute='error_enum')
    detail = fields.Str()
