from typing import List


class BaseCommand(object):
    """BaseCommand is the low-level representation
    of a command expressed at the CommandRequest
    interaction type.
        :::param component
        :::param capability
        ::param command
        ::param arguments"""

    def __init__(self, component: str, capability: str, command: str, arguments: List):
        self.component = component
        self.capability = capability
        self.command = command
        self.arguments = arguments or []
