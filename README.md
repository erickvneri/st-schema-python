# SmartThings Schema Connector Python SDK

The _SmartThings Schema Connector Python SDK_ is a package that simplify resources of
**Schema Connector** instances through built-in interfaces.

## Installation

Clone this repository.

    git clone https://github.com/erickvneri/st-schema-python

Copy the `stschema` package into your working directory.

    cp -r ./st-schema-python/stschema /your/working/directory/

---

## SchemaConnector structure

Using **class inheritance**, we'll gain access to a series of resources to control the request and response data of _Interaction types_.

```python
from stschema import SchemaConnector


class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

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
        # The state_refresh_handler gives access to
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
        # The interaction_result_handler provides
        # a description of the error triggered
        # between interaction type responses.
        pass
```

_**Note**: If any resource handler is not implemented but gets used by the `SchemaConnector.    interaction_handler` built-in method, a `NotImplementedError` exception will be raised._

## SchemaDevice definition.

SchemaDevice instance supporting the minimal requirements to create a virtual device at the _SmartThings ecosystem_.

1. Device definition using the SchemaDevice class and the `set_mn` instance method to specify the manufacturer's information:
```python
from stschema import SchemaDevice


my_device = SchemaDevice(
    '{{external_device_id}}',
    '{{friendly_name}}',
    '{{device_handler_type}}'
)

my_device.set_mn(
    '{{manufacturer_name}}',
    '{{model_name}}'
)
```
2. States definition applying the `set_state` instance method:

```python
my_device.set_state(
    'st.{{capability_id}}',
    '{{attribute}}',
    '{{value}}'
)
```

### SchemaConnector as a web-service with _Flask_.

Using _Flask_, the web development framework, here's an example of an application that will host our Webhook endpoint and our _SchemaConnector_ instance
to create and control a virtual switch at the _SmartThings_ app.

```python
from flask import Flask, request
from stschema import SchemaConnector, SchemaDevice


# MyConnector definition
class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

    def discovery_handler(self, request_id):
        # Device definition using the SchemaDevice class
        my_switch = SchemaDevice(
            '1a2b3c4d-x97y98z99',
            'Office light',
            'c2c-switch'
        )
        my_switch.set_mn(
            'Switch Mn Example',
            'Model X1'
        )
        declared_devices = [my_switch]
        return self.discovery_response(declared_devices, request_id)

    def state_refresh_handler(self, devices, request_id):
        # State Refresh Request information
        device_id = devices[0]['externalDeviceId']

        # SchemaDevice Instance
        # and state definition.
        my_device = SchemaDevice(device_id)
        my_device.set_state(
            'st.switch',
            'switch',
            'on'
        )
        # Collection of devices, in this
        # case, just my_device instance.
        filtered_devices = [my_device]
        return self.state_refresh_response(filtered_devices, request_id)

    def command_handler(self, devices, request_id):
        # Command Request information
        device_id = devices[0]['externalDeviceId']
        command = devices[0]['commands'][0]

        # SchemaDevice instance applying
        # the updated state as commanded.
        my_device = SchemaDevice(device_id)
        my_device.set_state(
            'st.switch',
            'switch',
            command['command'] # 'on' or 'off'
        )
        # Updated device passed as a list argument.
        updated_device = [my_device]
        return  self.command_response(updated_device, request_id)


# Flask app definition
app = Flask(__name__)
# MyConnector instance
my_connector = MyConnector()


# Endpoint definition
@app.route('/webhook-endpoint', methods=['POST'])
def main():
    # Request JSON body
    json_data = request.get_json()
    # The interaction_handler built-in method
    # will handle the JSON data and call every
    # resource accordingly.
    return my_connector.interaction_handler(json_data)


if __name__ == '__main__':
    app.run('localhost', 8000)

```

_Notice that the `SchemaConnector.grant_callback_access` built-in resource hasn't been implemented. In this case, when the Schema Connector instance gets integrated for the first time at the SmartThings ecosystem, the `NotImplementedError` exception will be raised as following:_

    ...
    NotImplementedError: [grant_callback_access] - Interaction resource handler not implemented


---
To learn more about _SmartThings Schema Connector_ integrations, please visit our _[main documentation](https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/schema-basics.html)_
or share your questions at our _[Community Forums](https://community.smartthings.com/c/developer-programs)_.
