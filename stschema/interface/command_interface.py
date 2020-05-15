from stschema.base.handlers import VoidCommand, BaseCommand
from stschema.base.device import BaseState
from stschema.base.util import CapabilityAttribute


class CommandHandler(BaseCommand):
    """The CommandHandler interface inherits
    from the BaseCommand class. It receives
    a dictionary of the command executed and
    received at the CommandRequest:
        :::param command: dict
        e.g.
        {
            'component': 'main'
            'capability': 'st.switch'
            'command': 'off'
            'arguments': []
        }"""

    def __init__(self, command: dict):
        BaseCommand.__init__(
            self,
            component=command.get('component'),
            capability=command.get('capability'),
            command=command.get('command'),
            arguments=command.get('arguments')
        )

    def get_state(self):
        """Returns a new device state based
        on the information of the command
        received at te CommandRequest."""

        new_state = None
        if not self.arguments:
            command = VoidCommand(self.command)
            capability = CapabilityAttribute(self.capability)
            new_state = BaseState(
                component=self.component,
                capability=capability.value,
                attribute=capability.name,
                value=command.name,
                unit=None
            )
        elif len(self.arguments) == 1:
            capability = CapabilityAttribute(self.capability)
            new_state = BaseState(
                component=self.component,
                capability=capability.value,
                attribute=capability.name,
                value=self.arguments[0],
                unit=None
            )
        return new_state
