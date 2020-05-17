from enum import Enum


class VoidCommand(Enum):
    """The VoidCommand Enumerator class is
    designed for commands that doesn't support
    additional values as arguments when receiving
    a CommandRequest interaction type."""

    on = 'on'
    off = 'off'
    open = 'open'
    closed = 'close'
