# ST-Schema Python SDK <img src="https://images.samsung.com/is/image/samsung/p5/au/faq/smartthings/smartthings-icon.png?$ORIGIN_PNG$" width=35><img src="http://clipart-library.com/images_k/python-logo-transparent/python-logo-transparent-5.png" width=35>

The ST-Schema Python SDK is a package that helps to simplify the development of 
**Schema Connectors** with ordered resources through interfaces.

## Installation

For macOS or Linux distributions:

    pyhton3 -m pip install st-schema-python
    
For Windows OS:

    python -m pip install st-schema-python
    
## Getting started

This is a basic use-case example of the Device Interface that this SDK provides to 
improve the organization of resources.

1. First, we define the device's main attributes:
    ```python
    from stschema.interface import Device
    
    
    device_example = Device(
        external_device_id='xxx123',
        friendly_name='my_first_device_example', 
        device_unique_id='xxx-yyy-zzz',
        device_cookie='cookie-example',
        device_handler_type='device-profile-id'
    )
    
    device_example.set_mn(
        manufacturer_name='Example IoT co.',
        model_name='example office lightning',
        hw_version='1.0.1',
        sw_version='2.0'
    )
    device_example.set_context(
        room_name='office',
        groups=['light', 'office', 'illumination'],
        categories=['light', 'illumination']
    )
    ```
2. Now, we define the **capabilities** and **state** of our device:

    ```python
    device_example.set_state(
        capability='healthCheck',
        attribute='healthStatus',
        value='online'
    )
    device_example.set_state(
        capability='switch',
        attribute='switch',
        value='on'
    )
    ``` 
3. Finally, we pass our device as argument to our SchemaConnector instance and we'll 
get access to a series of handlers. See below:

    ```python
    from stschema import SchemaConnector
    from some_where import device_example
    
    
    devices = [device_example]
    connector = SchemaConnector(devices)
    
    # Discovery Request handler
    if interaction_type == 'discoveryRequest':
       return connector.discovery_handler(request_id)
   
    # State Refresh Request handler
    elif interaction_type == 'stateRefreshRequest':
       return connector.state_handler(devices, request_id)
    
    # Command Request handler
    elif interaction_type == 'commandRequest':
       return connector.command_handler(device_command, request_id)
    ```

---
To learn more about _SmartThings Schema Connectors_, please check the _[main documentation](https://smartthings.developer.samsung.com/docs/devices/smartthings-schema/schema-basics.html)_
or visit our _[Community Forums](https://community.smartthings.com/)_.
