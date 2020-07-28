from marshmallow import Schema, fields
from stschema.util import (
    HeadersSchema,
    BaseResponse,
    BaseError,
    BaseErrorSchema
)


class GlobalErrorResponse(BaseResponse):
    """
    The GlobalErrorResponse is an object
    representation of a global-contextual
    error.

        :::param interaction_type (required)
        :::param request_id (required)
        :::param global_error: BaseError instance.
    """
    def __init__(self, interaction_type: str, request_id: str, global_error: object) -> 'GlobalErrorResponse':
        BaseResponse.__init__(self, interaction_type, request_id)
        # BaseError instance
        self.global_error = global_error


class GlobalErrorSchema(Schema):
    """
    The GlobalErrorSchema handles
    the serialization of the
    GlobalErrorResponse classsupporting
    the nested BaseErrorSchema and
    HeadersSchema.
    It converts Snake Case attributes
    to Camel Case format following REST
    formatting conventions for JSON
    string objects.
    """
    headers = fields.Nested(HeadersSchema, attribute='headers')
    globalError = fields.Nested(BaseErrorSchema, attribute='global_error')
