import pytest
from tests.device_fixture import SchemaDeviceFixture
from stschema.schema_response import SchemaResponse
from stschema import SchemaDevice
from stschema.schema_device.schemas import (
    DeviceDiscoverySchema,
    DeviceStateSchema,
    DeviceErrorSchema
)


#######################################################################
############## Main SchemaDevice Instance Fixture #####################
#######################################################################
@pytest.fixture(name='device_fixture', scope='class')
def device_fixture():
    device = SchemaDeviceFixture(error_state=False)
    return device

#######################################################################
########### ErrorState SchemaDevice Instance Fixture ##################
#######################################################################
# This fixture doesn't use the main
# device_fixture since it is creating
# a new instance of the SchemaDeviceFixture
# class passing error_state = True to
# create a DeviceError state.
@pytest.fixture(name='error_state_device', scope='class')
def error_state_device():
    device = SchemaDeviceFixture(error_state=True)
    schema = DeviceErrorSchema()
    return schema.dump(device), device


#********************Interaction Type Fixtures*************************
#######################################################################
#################### Device Discovery Fixture #########################
#######################################################################
# SchemaDevice serialization using
# the DeviceDiscoverySchema class.
@pytest.fixture(name='discovery_device', scope='class')
def discovery_device(device_fixture):
    schema = DeviceDiscoverySchema()
    return schema.dump(device_fixture)

#######################################################################
####################### Device State Fixture ##########################
#######################################################################
# SchemaDevice serialization using
# the DeviceStateSchema class.
@pytest.fixture(name='state_device', scope='class')
def state_device(device_fixture):
    schema = DeviceStateSchema()
    return schema.dump(device_fixture)


#********************Interaction Type Fixtures*************************
#######################################################################
#################### Discovery Response Fixture #######################
#######################################################################
@pytest.fixture(name='discovery_response_fixture', scope='class')
def discovery_response_fixture(device_fixture):
    discovery_response = SchemaResponse.discovery_response([device_fixture], 'request_id_example')
    return discovery_response

#######################################################################
################# State Refresh Response Fixture ######################
#######################################################################
@pytest.fixture(name='state_refresh_response_fixture', scope='class')
def state_refresh_response_fixture(device_fixture):
    state_refresh_response = SchemaResponse.state_refresh_response([device_fixture], 'request_id_example')
    return state_refresh_response

#######################################################################
#################### Command Response Fixture #########################
#######################################################################
@pytest.fixture(name='command_response_fixture', scope='class')
def command_response_fixture(device_fixture):
    command_response = SchemaResponse.command_response([device_fixture], 'request_id_example')
    return command_response