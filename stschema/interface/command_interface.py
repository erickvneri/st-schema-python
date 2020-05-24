from stschema.base.handlers import VoidCommand, BaseCommand
from stschema.base.device import BaseState
from stschema.base.util import CapabilityAttribute


class CommandHandler(BaseCommand):
    """The CommandHandler interface inherits
    its attributes from the BaseCommand class."""

    def __init__(self, command: dict):
        BaseCommand.__init__(
            self,
            component=command.get('component'),
            capability=command.get('capability'),
            command=command.get('command'),
            arguments=command.get('arguments')
        )

    def get_state(self):
        """This instance method converts commands
        into device's states."""

        new_state = None
        if not self.arguments:
            """If command received has
            no arguments."""
            capability = CapabilityAttribute(self.capability)
            command = VoidCommand(self.command)
            new_state = BaseState(
                component=self.component,
                capability=capability.value,
                attribute=capability.name,
                value=command.name,
                unit=None
            )

        elif type(self.arguments[0]) is not dict:
            """If command received has 
            a single argument as value."""
            capability = CapabilityAttribute(self.capability)
            new_state = BaseState(
                component=self.component,
                capability=capability.value,
                attribute=capability.name,
                value=self.arguments[0],
                unit=None
            )

        elif type(self.arguments[0]) is dict:
            """If command received has 
            multiple attributes as arguments."""
            capability = CapabilityAttribute(self.capability)
            args = self.arguments[0]
            new_state = []
            for attribute, value in args.items():
                new_state.append(BaseState(
                    component=self.component,
                    capability=capability.value,
                    attribute=attribute,
                    value=value,
                    unit=None
                ))
        return new_state
