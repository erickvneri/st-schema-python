# SmartThings Schema Connector Python SDK

The _SmartThings Schema Connector Python SDK_ is a package that helps to simplify resources of
**Schema Connector** instances through built-in interfaces.

## Installation

For macOS or Linux distributions:

    pyhton3 -m pip install st-schema-python

For Windows OS:

    python -m pip install st-schema-python

## Getting started

This is a basic use-case example of the SchemaDevice interface supporting the minimal requirements.

1. Device definition using the SchemaDevice class and the `set_mn` instance method to specify the manufacturer's information.
```python
from stschema import SchemaDevice


device_example = SchemaDevice(
    '{{external_device_id}}',
    '{{friendly_name}}',
    '{{device_handler_type}}'
)

device_example.set_mn(
    '{{manufacturer_name}}',
    '{{model_name}}',
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
