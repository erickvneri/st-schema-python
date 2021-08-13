# SmartThings Schema Connector Python SDK

The _SmartThings Schema Connector Python SDK_ is a package that simplify resources of
**Schema Connector** instances through built-in interfaces.

### Installation

Install it using `pip`:

    pip install st-schema-python

---

### SchemaConnector structure

Using **class inheritance**, we'll gain access to a series of resources to control the request and response data of _Interaction types_.

```python
from stschema import SchemaConnector


class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

    def discovery_handler(self, request_id, access_token):
        # The discovery_handler built-in method
        # gives access to discoveryRequest data.
        #
        # SchemaDevice instances must be passed
        # as a list argument to discovery_response
        # built-in method.
        declared_devices = [...]
        return self.discovery_response(declared_devices, request_id)

    def state_refresh_handler(self, devices, request_id, access_token):
        # The state_refresh_handler gives access to
        # stateRefreshRequest data.
        # A filtered list of SchemaDevice instances
        # must be passed as response to the
        # state_refresh_response built-in method.
        filtered_devices = [...]
        return self.state_refresh_response(filtered_devices, request_id)

    def command_handler(self, devices, request_id, access_token):
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

_**Note**: If any resource handler is not implemented but gets used by the `SchemaConnector. interaction_handler` built-in method, a `NotImplementedError` exception will be raised._

---

### SchemaDevice definition.

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

---

### SchemaConnector as a web-service with the _Http.server_ built-in module.

Using the Python's built-in module _Http.server_, here's an example of an application that will host our Webhook endpoint and our _SchemaConnector_ instance
to create and control a virtual switch at the _SmartThings_ app.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from stschema import SchemaConnector, SchemaDevice
import json


# MyConnector definition
class MyConnector(SchemaConnector):
    def __init__(self, *opts):
        SchemaConnector.__init__(self, enable_logger=True)

    def discovery_handler(self, request_id, access_token):
        # Device definition using the SchemaDevice class
        my_switch = SchemaDevice(  # Device info
            'xyz_example_id_xyz',
            'Office light',
            'c2c-switch')
        my_switch.set_mn(  # Manufacturer info
            'Switch Mn Example',
            'Model X1')
        my_switch.set_context(
            'Office',
            [],
            ['light'])

        declared_devices = [my_switch]
        return self.discovery_response(declared_devices, request_id)

    def state_refresh_handler(self, devices, request_id, access_token):
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

    def command_handler(self, devices, request_id, access_token):
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

    def interaction_result_handler(self, interaction_result: dict, origin: str):
        print(interaction_result, origin)
        pass


# MyConnector instance
my_connector = MyConnector()


class WebhookServer(BaseHTTPRequestHandler):
    """
    This class will serve as endpoint to handle
    the POST Http Requests sent to the
    registered Target Url. Notice that this
    webhook instance won't differentiate endpoints.
    """
    def do_POST(self):
        # POST Http Request handler.
        content_length = int(self.headers['Content-Length'])
        req_body = self.rfile.read(content_length).decode('utf-8')
        # getting JSON body from request.
        json_data = json.loads(req_body)
        return self._set_response(json_data)

    def _set_response(self, data):
        # interaction_handler is a
        # SchemaConnector built-in method
        # that takes the JSON body as
        # argument.
        connector_handler = my_connector.interaction_handler(data)
        # JSON Interaction types responses
        res_data = json.dumps(connector_handler).encode('utf-8')
        self._set_headers()
        self.wfile.write(res_data)

    def _set_headers(self):
        # Declare application/json
        # headers to parse JSON string
        # response.
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('', 8000)
    http = HTTPServer(server_address, WebhookServer)
    http.serve_forever()

```

_Notice that the `SchemaConnector.grant_callback_access` built-in resource hasn't been implemented. In this case, when the Schema Connector instance gets integrated for the first time at the SmartThings ecosystem, the `NotImplementedError` exception will be raised as following:_

    ...
    NotImplementedError: [grant_callback_access] - Interaction resource handler not implemented

---

### _Developer Note_.

Before pushing any updates into the _SmartThings Schema Connector Python SDK_, please install `pytest` and execute the follwing command to run the full _test suite_.

    python3 -m pytest -p no:cacheprovider

---

To learn more about _SmartThings Schema Connector_ integrations, visit the _[SmartThings Community Forums](https://community.smartthings.com/c/developer-programs)_.
