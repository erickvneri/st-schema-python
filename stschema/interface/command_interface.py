from stschema.base.handlers import VoidCommand, BaseCommand
from stschema.base.device import BaseState

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

        # if self.arguments == []:
        #     command = VoidCommand(self.command)
        #     new_state = BaseState(
        #         component='main',
        #         capability=self.capability,
        #         # attribute=FIXME: CAPABILITY ENUM,
        #         value=command.name,
        #         unit=None
        #     )
        pass
