import pytest
from marshmallow import Schema, fields


class CommandSchema(Schema):
    component = fields.Str()
    capability = fields.Str()
    command = fields.Str()
    arguments = fields.List(fields.Field)


class CommandRequest(Schema):
    def __init__(self):
        Schema.__init__(self, unknown='EXCLUDE', many=True)

    externalDeviceId = fields.Str(attribute='external_device_id')
    commands = fields.List(fields.Nested(CommandSchema))


class TestCommandHandler(object):
    @pytest.fixture
    def command(self):
        command = {
            "headers": {
                "schema": "st-schema",
                "version": "1.0",
                "interactionType": "commandRequest",
                "requestId": "abc-123-456"
            },
            "authentication": {
                "tokenType": "Bearer",
                "token": "token-received during oauth from partner"
            },
            "devices": [
                {
                    "externalDeviceId": "partner-device-id",
                    "deviceCookie": {
                        "lastcookie": "cookie value"
                    },
                    "commands": [
                        {
                            "component": "main",
                            "capability": "st.colorControl",
                            "command": "setColor",
                            "arguments": [
                                {
                                    "saturation": 91,
                                    "hue": 0.8333333333333334
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        yield command

    def command_tracker(self, command):
        schema = CommandRequest()
        command = schema.load(command['devices'])
        cmd = command[0]['commands']
        return cmd

    def test_command_request_schema(self, command):
        res = CommandRequest().load(command['devices'])
        assert res

    def test_cmd_tracker(self, command):
        c = self.command_tracker(command)
        print(c)

