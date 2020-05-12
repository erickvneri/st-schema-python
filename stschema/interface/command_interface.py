from stschema.base.handlers import VoidCommand, BaseCommand


class CommandHandler(BaseCommand):
    """The CommandHandler interface inherits
    from the BaseCommand class. It receives
    a dictionary of the command executed and
    received at the CommandRequest:
        :::param command: dict
        e.g.
        {
            'component': 'main'
            'capability': 'st.colorControl'
            'command': 'setControl'
            'arguments': [{
                'saturation': 99,
                'hue': 66
            }]
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

        pass
