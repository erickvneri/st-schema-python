from enum import Enum


class VoidCommand(Enum):
    """The VoidCommand Enumerator is
    used to get the device's state value
    based on commands without arguments."""

    on = 'on'
    off = 'off'
    open = 'open'
    closed = 'close'
