class BaseDevice:
    """
    The BaseDevice class represents
    the basic metadata of a device
    integrations.
        :::param external_device_id
        :::param friendly_name
        :::param device_handler_type
        :::param device_cookie
        :::param unique_device_id
    """

    def __init__(self, external_device_id: str, friendly_name: str, device_unique_id: str, device_cookie: str, device_handler_type: str) -> 'BaseDevice':
        self.external_device_id = external_device_id
        self.friendly_name = friendly_name
        self.device_unique_id = device_unique_id
        self.device_cookie = device_cookie
        self.device_handler_type = device_handler_type
