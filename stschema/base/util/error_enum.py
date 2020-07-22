import enum


class StateErrorEnum(enum.Enum):
    """The StateErrorEnum class
    specifies the concept of the
    error ocurred specifically for
    devices' states."""

    CAPABILITY_NOT_SUPPORTED = 'CAPABILITY-NOT-SUPPORTED'
    DEVICE_DELETED = 'DEVICE-DELETED'
    DEVICE_UNAVAILABLE = 'DEVICE-UNAVAILABLE'
    RESOURCE_CONSTRAINT_VIOLATION = 'RESOURCE-CONSTRAINT-VIOLATION'


class GlobalErrorEnum(enum.Enum):
    """The GlobalErrorEnum class
    specifies the concept of the
    error ocurred in a global
    context (e.g. access token used
    has expired -> TOKEN_EXPIRED enum)"""

    BAD_REQUEST = 'BAD-REQUEST'
    INTEGRATION_DELETED = 'INTEGRATION-DELETED'
    INVALID_CLIENT = 'INVALID-CLIENT'
    INVALID_CLIENT_SECRET = 'INVALID-CLIENT-SECRET'
    INVALID_CODE = 'INVALID-CODE'
    INVALID_INTERACTION_TYPE = 'INVALID-INTERACTION-TYPE'
    INVALID_TOKEN = 'INVALID-TOKEN'
    TOKEN_EXPIRED = 'TOKEN-EXPIRED'
    UNSUPPORTED_GRANT_TYPE = 'UNSUPPORTED-GRANT-TYPE'