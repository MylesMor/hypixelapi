Getting Started
======================================
To install run:

``pip install hypixelapi``

Getting Started
-------------------

First, run /api on the Hypixel server to get your own key.

```
from hypixelapi import HypixelAPI
api = HypixelAPI('your-key-here')
response = api.get_player_json('uuid')
print(response)
```

For detailed documentation of each function: .. _rst_tutorial:
