import pytest
from datetime import datetime
from stschema.interface.schemas import DeviceCommandMapper


class TestDeviceCommandMapperSchema(object):
    @pytest.fixture
    def device_cmd(self):
        cmd = dict(
            externalDeviceId='as5d4fds1a3',
            deviceCookie={'cookie': datetime.now().strftime('%Y/%m/%d %H:%M:%:S')},
            commands=[{
                "component": "main",
                "capability": "st.colorControl",
                "command": "setColor",
                "arguments": [
                    {
                        "saturation": 91,
                        "hue": 0.8333333333333334
                    }]
            }]
        )
        yield cmd

    def test_command_mapper_documentation(self):
        assert DeviceCommandMapper
        assert DeviceCommandMapper.__doc__
        assert len(DeviceCommandMapper.__doc__) != 0

    def test_command_mapper_composition(self):
        assert DeviceCommandMapper()
        assert DeviceCommandMapper().fields['externalDeviceId']
        assert DeviceCommandMapper().fields['commands']

    def test_map_command(self, device_cmd):
        schema = DeviceCommandMapper()
        mapped_cmd = schema.load(device_cmd)
        print(mapped_cmd)
        assert mapped_cmd
        assert mapped_cmd['external_device_id']
        assert type(mapped_cmd['external_device_id']) is str
        assert mapped_cmd['commands']
        assert type(mapped_cmd['commands']) is list

    def test_command_mapper_key_error(self):
        with pytest.raises(KeyError):
            assert DeviceCommandMapper().fields['secret']
            assert DeviceCommandMapper().fields['secretId']
            assert DeviceCommandMapper().fields['clientSecret']
            assert DeviceCommandMapper().fields['userId']
            assert DeviceCommandMapper().fields['password']

