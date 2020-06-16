from typing import List


class BaseCommand:
    """The BaseCommand class is the basic
    representation of a command emitted by
    the SmartThings Cloud.
        :::param component
        :::param capability
        ::param command
        ::param arguments"""

    def __init__(self, component: str, capability: str, command: str, arguments: List[any]):
        self.component = component
        self.capability = capability
        self.command = command
        self.arguments = arguments or []
