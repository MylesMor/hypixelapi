Getting Started
======================================

Installation
-----------------

To install run:

``pip install hypixelapi``


Try it out!
-------------------

First, run /api on the Hypixel server to get your own key.

.. code-block:: python
  :linenos:

  from hypixelapi import HypixelAPI
  api = HypixelAPI('your-key-here')
  response = api.get_player_json('uuid')
  print(response)


For detailed documentation of each function see the API documentation.
