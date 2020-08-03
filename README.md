# SmartThings Schema Connector Python SDK

The _SmartThings Schema Connector Python SDK_ is a package that simplify resources of
**Schema Connector** instances through built-in interfaces.


## Installation (_Expected use - WIP_)

For macOS or Linux distributions:

    pyhton3 -m pip install st-schema-python

For Windows OS:

    python -m pip install st-schema-python

---

## SchemaConnector structure

Using class inheritance, we'll gain access to a series of resources to control the request and response data of _Interaction types_.

```python
from stschema import SchemaConnector


class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logs=True)

    def discovery_handler(self, request_id):
        # The discovery_handler built-in method
        # gives access to discoveryRequest data.
        #
        # SchemaDevice instances must be passed
        # as a list argument to discovery_response
        # built-in method.
        declared_devices = [...]
        return self.discovery_response(declared_devices, request_id)

    def state_refresh_handler(self, devices, request_id):
        # the state_refresh_handler gives access to
        # stateRefreshRequest data.
        # A filtered list of SchemaDevice instances
        # must be passed as response to the
        # state_refresh_response built-in method.
        filtered_devices = [...]
        return self.state_refresh_response(filtered_devices, request_id)

    def command_handler(self, devices, request_id):
        # The command_handler gives access to the
        # commandRequest data.
        # A list of an updated SchemaDevice instance
        # must be passed as response to the
        # command_response built-in method.
        updated_device = [...]
        return  self.command_response(updated_device, request_id)

    def grant_callback_access(self, callback_authentication, callback_urls):
        # Built-in method triggered with the
        # grantCallbackAccess interaction type.
        pass

    def integration_deleted(self, callback_authentication):
        # Built-in method triggered with the
        # integrationDeleted interactionType.
        pass

    def interaction_result_handler(self, interaction_result, origin):
        # Interaction Result Handler provides
        # a description of the error ocurred
        # between interaction type responses.
        pass
```

_**Note**: If any resource handler is not implemented but gets used by the `SchemaConnector._interaction_handler` built-in method, a `NotImplementedError` exception will be raised._

## SchemaDevice definition.

Below there's a SchemaDevice instance supporting the minimal requirements to create a device at the _SmartThings ecosystem_.

1. Device definition using the SchemaDevice class and the `set_mn` instance method to specify the manufacturer's information:
```python
from stschema import SchemaDevice


device_example = SchemaDevice(
    '{{external_device_id}}',
    '{{friendly_name}}',
    '{{device_handler_type}}'
)

device_example.set_mn(
    '{{manufacturer_name}}',
    '{{model_name}}'
)
```
2. States definition applying the `set_state` instance method:

```python
device_example.set_state(
    'st.{{capability_id}}',
    '{{attribute}}',
    '{{value}}'
)
```

---
To learn more about _SmartThings Schema Connector_ integrations, please visit our _[main documentation](https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/schema-basics.html)_
or share your questions at our _[Community Forums](https://community.smartthings.com/c/developer-programs)_.
