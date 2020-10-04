"""
Test Suite over functionalities that
the SchemaDevice class interface provides.

Initial feature tested is the
flexibility of a Device
instantiation, supporting for
straight (*args) and key word
(**kwargs) arguments.

Some Test-to-Fail test cases have
been included. These Exceptions help
develoeprs to improve creation of
Device instances.
"""
import pytest
from stschema import SchemaDevice
from stschema.util.base_modules import ManufacturerInfo


class TestDeviceInterface:
    """
    Test Suite on Device class interface.

    Index:
        - TestSchemaDeviceClassAttributes
        - TestDeviceDefinition
        - TestManufacturerInfo
        - TestDeviceContext
        - TestSetState
        - TestDeviceError
    """
    class TestSchemaDeviceClassAttributes:
        # Test case on the construction
        # of the Device class interface.
        def test_documentation(self):
            # Class documentation
            assert SchemaDevice.__doc__
            assert len(SchemaDevice.__doc__) > 0

        def test_public_methods(self):
            # Public methods
            assert SchemaDevice.set_context
            assert SchemaDevice.set_mn
            assert SchemaDevice.set_state
            assert SchemaDevice.set_error_state


    class TestDeviceDefinition:
        # Test case on the initial Device
        # instance.
        def test_device_instance_from_args(self):
            # Base definition from
            # straight arguments (*args).
            device = SchemaDevice(
                'external_device_id_arg',
                'friendly_name_arg',
                'device_handler_type_arg',
                'device_unique_id_arg',
                'device_cookie_arg'
            )
            assert device.external_device_id == 'external_device_id_arg'
            assert device.friendly_name == 'friendly_name_arg'
            assert device.device_handler_type == 'device_handler_type_arg'
            assert device.device_unique_id == 'device_unique_id_arg'
            assert device.device_cookie.cookie == 'device_cookie_arg'

        def test_device_instance_from_kwargs(self):
            # Base definition from
            # key word arguments (**kwargs)
            device = SchemaDevice(
                external_device_id='external_device_id_kwarg',
                friendly_name='friendly_name_kwarg',
                device_handler_type='device_handler_type_kwarg',
                device_unique_id='device_unique_id_kwarg',
                device_cookie='device_cookie_kwarg'
            )
            assert device.external_device_id == 'external_device_id_kwarg'
            assert device.friendly_name == 'friendly_name_kwarg'
            assert device.device_handler_type == 'device_handler_type_kwarg'
            assert device.device_unique_id == 'device_unique_id_kwarg'
            assert device.device_cookie.cookie == 'device_cookie_kwarg'

        def test_type_error_unexpected_arg(self):
            # Test for unexpected arguments
            # when defining main instance
            # attributes.
            with pytest.raises(TypeError):
                SchemaDevice(
                    'external_device_id_arg',
                    'friendly_name_arg',
                    'device_handler_type_arg',
                    'device_unique_id_arg',
                    'device_cookie_arg',
                    'UNEXPECTED_ARGUMENT_1',
                    'UNEXPECTED_ARGUMENT_2'
                )


    class TestManufacturerInfo:
        # Test case on the definition of the
        # device's manufacturer info attributes.
        def test_manufacturer_info_from_args(self):
            # Manufacturer Info default definition
            # using straight arguments. Checking order
            # and reliability of handler.
            device = SchemaDevice()
            device.set_mn(
                'manufacturer_info_arg',
                'model_name_arg',
                'hardware_version_arg',
                'software_version_arg'
            )
            assert isinstance(device.manufacturer_info, ManufacturerInfo)
            assert device.manufacturer_info.manufacturer_name == 'manufacturer_info_arg'
            assert device.manufacturer_info.model_name == 'model_name_arg'
            assert device.manufacturer_info.hw_version == 'hardware_version_arg'
            assert device.manufacturer_info.sw_version == 'software_version_arg'

        def test_manufacturer_info_from_kwargs(self):
            # Manufacturer Info definition
            # from key word arguments (**kwargs).
            device = SchemaDevice()
            device.set_mn(
                manufacturer_name='manufacturer_info_kwarg',
                model_name='model_name_kwarg',
                hw_version='hardware_version_kwarg',
                sw_version='software_version_kwarg'
            )
            assert isinstance(device.manufacturer_info, ManufacturerInfo)
            assert device.manufacturer_info.manufacturer_name == 'manufacturer_info_kwarg'
            assert device.manufacturer_info.model_name == 'model_name_kwarg'
            assert device.manufacturer_info.hw_version == 'hardware_version_kwarg'
            assert device.manufacturer_info.sw_version == 'software_version_kwarg'


        def test_type_error_unexpected_arguments(self):
            # Test for unexpected arguments
            # when defining Manufacturer's
            # Info attributes.
            with pytest.raises(TypeError):
                device = SchemaDevice()
                device.set_mn(
                    'manufacturer_info_arg',
                    'model_name_arg',
                    'hardware_version_arg',
                    'software_version_arg',
                    'UNEXPECTED_ARGUMENT_1',
                    'UNEXPECTED_ARGUMENT_2'
                )


    class TestDeviceContext:
            # Test case on the definition of the
            # Device Context attributes for a Device
            # instance.
            def test_device_context_from_args(self):
                # Device Context default definition
                # using straight arguments. Checking order
                # and reliability of handler.
                device = SchemaDevice()
                device.set_context(
                    'room_name_arg',
                    ['groups', 'list', 'args'],
                    ['categories', 'list', 'args']
                )
                assert device.device_context.room_name == 'room_name_arg'
                assert isinstance(device.device_context.groups, list)
                assert device.device_context.groups == ['groups', 'list', 'args']
                assert isinstance(device.device_context.categories, list)
                assert device.device_context.categories == ['categories', 'list', 'args']

            def test_device_context_from_kwargs(self):
                # Device Context definition from
                # key word arguments (**kwargs).
                device = SchemaDevice()
                device.set_context(
                    room_name='room_name_kwarg',
                    groups=['groups', 'list', 'kwargs'],
                    categories=['categories', 'list', 'kwargs']
                )
                assert device.device_context.room_name == 'room_name_kwarg'
                assert isinstance(device.device_context.groups, list)
                assert device.device_context.groups == ['groups', 'list', 'kwargs']
                assert isinstance(device.device_context.categories, list)
                assert device.device_context.categories == ['categories', 'list', 'kwargs']

            def test_type_error_unexpected_arguments(self):
                # Test for unexpected arguments
                # when defining Device Context
                # attributes.
                with pytest.raises(TypeError):
                    device = SchemaDevice()
                    device.set_context(
                        'room_name_arg',
                        ['groups', 'list', 'args'],
                        ['categories', 'list', 'args'],
                        'UNEXPECTED_ARGUMENT'
                    )

            def test_type_error_list_arg_expected(self):
                # Test for unexpected type if
                # args passed are not list.
                with pytest.raises(TypeError):
                    device = SchemaDevice()
                    device.set_context(
                        'room_name_arg',
                        'groups_string_argument',
                        'categories_string_argument'
                    )


    class TestSetState:
        # Test Case on the definition of
        # states/capabilities as device's
        # state.
        def test_set_state_from_args(self):
            # State definition from straight
            # arguments.
            device = SchemaDevice()
            device.set_state(
                'capability_arg',
                'attribute_arg',
                'value_arg',
                'unit_arg',
                'component_arg'
            )
            assert device.states[0].capability == 'capability_arg'
            assert device.states[0].attribute == 'attribute_arg'
            assert device.states[0].value == 'value_arg'
            assert device.states[0].unit == 'unit_arg'
            assert device.states[0].component == 'component_arg'

        def test_set_state_from_kwargs(self):
            # State/Capability definition from
            # kwy word arguments (**kwargs).
            device = SchemaDevice()
            device.set_state(
                capability='capability_kwarg',
                attribute='attribute_kwarg',
                value='value_kwarg',
                unit='unit_kwarg',
                component='component_kwarg'
            )
            assert device.states[0].capability == 'capability_kwarg'
            assert device.states[0].attribute == 'attribute_kwarg'
            assert device.states[0].value == 'value_kwarg'
            assert device.states[0].unit == 'unit_kwarg'
            assert device.states[0].component == 'component_kwarg'

        def test_type_error_set_state_unexpected_arguments(self):
            # Test for unexpected arguments
            # when defining State/Capability
            # attributes.
            with pytest.raises(TypeError):
                device = SchemaDevice()
                device.set_state(
                    'capability_arg',
                    'attribute_arg',
                    'value_arg',
                    'unit_arg',
                    'component_arg',
                    'UNEXPECTED_ARGUMENT'
                )


    class TestDeviceError:
        # Test Case on DeviceError states.
        def test_error_state_default_definition(self):
            # Default Device Error state definition.
            device = SchemaDevice()
            device.set_error_state()
            assert device.device_error[0].error_enum == 'DEVICE-UNAVAILABLE'
            assert device.device_error[0].detail == 'unexpected error occurred.'

        def test_error_state_from_args(self):
            # Device Error state definition
            # from straight arguments (*args).
            device = SchemaDevice()
            device.set_error_state('CAPABILITY-NOT-SUPPORTED', 'detail_arg')
            assert device.device_error[0].error_enum == 'CAPABILITY-NOT-SUPPORTED'
            assert device.device_error[0].detail == 'detail_arg'

        def test_error_state_from_kwargs(self):
            # Device Error state definition
            # from key word arguments (**kwargs).
            device = SchemaDevice()
            device.set_error_state(error_enum='CAPABILITY-NOT-SUPPORTED', detail='detail_kwarg')
            assert device.device_error[0].error_enum == 'CAPABILITY-NOT-SUPPORTED'
            assert device.device_error[0].detail == 'detail_kwarg'

        def test_type_error_enum_not_supported(self):
            # Device Error Exception for
            # non-suppoted error enumerators.
            with pytest.raises(ValueError):
                device = SchemaDevice()
                device.set_error_state('ERROR-ENUM-NOT-SUPPORTED')


# Test Suite over the serialization
# of a SchemaDevice instance through
# the DeviceDiscoverSchema, DeviceStateSchema
# and DeviceErrorSchema.
#
# For this test suite, four fixtures
# will be used following the DRY
# principles on SchemaDevice instances.
#   - device_fixture
#   - discovery_device
#   - state_device
#   - error_state_device
from tests.device_fixture import SchemaDeviceFixture
from stschema.schema_device.schemas import (
    DeviceDiscoverySchema,
    DeviceStateSchema,
    DeviceErrorSchema
)

# Pytest Fixture definitions.
@pytest.fixture(name='device_fixture', scope='class')
def device_fixture():
    device = SchemaDeviceFixture(error_state=False)
    return device

@pytest.fixture(name='discovery_device', scope='class')
def discovery_device(device_fixture):
    schema = DeviceDiscoverySchema()
    return schema.dump(device_fixture)

@pytest.fixture(name='state_device', scope='class')
def state_device(device_fixture):
    schema = DeviceStateSchema()
    return schema.dump(device_fixture)

@pytest.fixture(name='error_state_device', scope='class')
def error_state_device():
    device = SchemaDeviceFixture(error_state=True)
    schema = DeviceErrorSchema()
    return schema.dump(device), device


class TestSchemaDeviceSerialization:
    """
    Test Suite on SchemaDevice serialization
    through Schemas.

    Index:
        - TestDiscoveryDevice
        - TestStateDevice
        - TestErrorStateDevice
    """
    class TestDiscoveryDevice:
        # Test case on DeviceDiscoverySchema
        # class attributes.
        #
        # Testing serialization
        # of SchemaDevice class.
        def test_device_discovery_scema_documentation(self):
            assert DeviceDiscoverySchema.__doc__
            assert len(DeviceDiscoverySchema.__doc__) != 0

        def test_device_discovery_schema(self):
            assert DeviceDiscoverySchema().declared_fields['externalDeviceId']
            assert DeviceDiscoverySchema().declared_fields['friendlyName']
            assert DeviceDiscoverySchema().declared_fields['deviceHandlerType']
            assert DeviceDiscoverySchema().declared_fields['deviceUniqueId']
            assert DeviceDiscoverySchema().declared_fields['deviceCookie']
            assert DeviceDiscoverySchema().declared_fields['manufacturerInfo']
            assert DeviceDiscoverySchema().declared_fields['deviceContext']

        def test_discovery_serialization(self, discovery_device, device_fixture):
            assert discovery_device
            assert discovery_device['externalDeviceId'] == device_fixture.external_device_id
            assert discovery_device['friendlyName'] == device_fixture.friendly_name
            assert discovery_device['deviceHandlerType'] == device_fixture.device_handler_type
            assert discovery_device['deviceUniqueId'] == device_fixture.device_unique_id
            assert discovery_device['deviceCookie']['cookie'] == device_fixture.device_cookie.cookie
            assert discovery_device['manufacturerInfo']['manufacturerName'] == device_fixture.manufacturer_info.manufacturer_name
            assert discovery_device['manufacturerInfo']['modelName'] == device_fixture.manufacturer_info.model_name
            assert discovery_device['manufacturerInfo']['hwVersion'] == device_fixture.manufacturer_info.hw_version
            assert discovery_device['manufacturerInfo']['swVersion'] == device_fixture.manufacturer_info.sw_version

    class TestStateDevice:
        # Test case on DeviceStateSchema
        # class attributes.
        #
        # Testing serialization of
        # SchemaDevice class.
        def test_device_state_schema_documentation(self):
            assert DeviceStateSchema.__doc__
            assert len(DeviceStateSchema.__doc__) != 0

        def test_device_state_schema(self):
            assert DeviceStateSchema().declared_fields['externalDeviceId']
            assert DeviceStateSchema().declared_fields['deviceCookie']
            assert DeviceStateSchema().declared_fields['states']

        def test_device_state_serialization(self, state_device, device_fixture):
            assert state_device['externalDeviceId'] == device_fixture.external_device_id
            assert state_device['deviceCookie']['cookie'] == device_fixture.device_cookie.cookie
            assert isinstance(state_device['states'], list) and isinstance(device_fixture.states, list)

        def test_device_states_consistency(self, state_device, device_fixture):
            # Test State: capability_1
            fixture_state_1 = list(filter(lambda state: state.capability == 'capability_1', device_fixture.states))
            device_state_1 = list(filter(lambda state: state['capability'] == 'capability_1', state_device['states']))
            assert device_state_1[0]['capability'] == fixture_state_1[0].capability
            assert device_state_1[0]['attribute'] == fixture_state_1[0].attribute
            assert device_state_1[0]['value'] == fixture_state_1[0].value
            assert device_state_1[0]['unit'] == fixture_state_1[0].unit
            assert device_state_1[0]['component'] == fixture_state_1[0].component

            # Test State: capability_2
            # No unit declared
            fixture_state_2 = list(filter(lambda state: state.capability == 'capability_2', device_fixture.states))
            device_state_2 = list(filter(lambda state: state['capability'] == 'capability_2', state_device['states']))
            assert device_state_2[0]['capability'] == fixture_state_2[0].capability
            assert device_state_2[0]['attribute'] == fixture_state_2[0].attribute
            assert device_state_2[0]['value'] == fixture_state_2[0].value
            assert device_state_2[0]['component'] == fixture_state_2[0].component
            # KeyError raised at SchemaDevice
            # serialization due to undeclared
            # unit attribute.
            # AttributeError raised at SchemaDevice
            # objcet due to undeclared unit attribute.
            with pytest.raises(KeyError):
                assert device_state_2[0]['unit']
            with pytest.raises(AttributeError):
                assert fixture_state_2[0].unit

            # Test State: capability_3
            # No component declared
            # No unit declared
            fixture_state_3 = list(filter(lambda state: state.capability == 'capability_3', device_fixture.states))
            device_state_3 = list(filter(lambda state: state['capability'] == 'capability_3', state_device['states']))
            assert device_state_3[0]['capability'] == fixture_state_3[0].capability
            assert device_state_3[0]['attribute'] == fixture_state_3[0].attribute
            assert device_state_3[0]['value'] == fixture_state_3[0].value
            assert device_state_3[0]['component'] == fixture_state_3[0].component
            # KeyError raised at SchemaDevice
            # serialization due to undeclared
            # unit attribute.
            # AttributeError raised at SchemaDevice
            # objcet due to undeclared unit attribute.
            with pytest.raises(KeyError):
                assert device_state_3[0]['unit']
            with pytest.raises(AttributeError):
                assert fixture_state_3[0].unit


    class TestErrorStateDevice:
        # Test case on DeviceErrorSchema
        # class attributes.
        #
        # Testing serialization of SchemaDevice
        # supporting a state error enumerator.
        def test_device_error_state_schema_documentation(self):
            assert DeviceErrorSchema.__doc__
            assert len(DeviceErrorSchema.__doc__) != 0

        def test_device_error_schema(self):
            assert DeviceErrorSchema().declared_fields['externalDeviceId']
            assert DeviceErrorSchema().declared_fields['deviceError']

        def test_device_error_state_serialization(self, error_state_device):
            error_state_device, device_fixture = error_state_device
            assert error_state_device['externalDeviceId'] == device_fixture.external_device_id
            assert isinstance(error_state_device['deviceError'], list) and \
                isinstance(device_fixture.device_error, list)
            assert error_state_device['deviceError'][0]['errorEnum'] == \
                device_fixture.device_error[0].error_enum
            assert error_state_device['deviceError'][0]['detail'] == \
                device_fixture.device_error[0].detail

        def test_device_error_schema_unsupport_states_attr(self, error_state_device):
            error_state_device, device_fixture = error_state_device
            # SchemaDevice can support states and
            # error states instances.
            assert device_fixture.states
            assert isinstance(device_fixture.states, list)
            # DeviceErrorSchema serialized object
            # won't support such values.
            with pytest.raises(KeyError):
                assert error_state_device['states']
            with pytest.raises(KeyError):
                assert isinstance(error_state_device['states'], list)
