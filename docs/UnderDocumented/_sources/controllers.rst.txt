=====================
Controllers
=====================

Interact Controller
--------------------

Important Notes
================

The interact controller will interact with the station you're infront of while using the take_actions method.

.. code-block:: python

    actions.chosen_action = ActionType.interact

Decay Controller
-----------------

Lore
=======

A Pizza and topping in real life do expire over of course of time and are unuseable,
So is in the game you these item that become more decay and not useable later on, and disappear.

Note
======

The items held by the player have a decay and once the item worth reaches 0 it disappears.
The infestation event speeds up decay on everything. See :doc:`stats` to find the decay rate


Movement Controller
--------------------

Important Notes
================

The Movement controller will move the cooks around the kitchen. The cooks can only move one tile at a time and to tiles which 
are not occupied nor wet.

.. code-block:: python

    # Moving up
    # cook current position is (3,3)
    action.chosen_action = ActionType.Move.up
    # cook current position is (2,3)

.. code-block:: python

    # Moving down
    # cook current position is (3,3)
    action.chosen_action = ActionType.Move.down
    # cook current position is (4,3)

.. code-block:: python

    # Moving left
    # cook current position is (3,3)
    action.chosen_action = ActionType.Move.left
    # cook current position is (3,2)

.. code-block:: python

    # Moving right
    # cook current position is (3,3)
    action.chosen_action = ActionType.Move.right
    # cook current position is (3,4)

Oven Controller
----------------

Important Notes
================

The oven controller will cook the pizza that will get burnt if it stay in the oven too long. The Oven will stop cooking due to the 
electrical event so you need to be careful of when the Oven is on or off. See :doc:`stats` for how long it takes to bake.


Wet tiles Controller
---------------------

Important Notes
================

The wet tiles controller will make certain tiles so wet that cook will not be able to walk onto those tiles.
This will only occur in flooding event. If none of the wet tile presets are valid, the event will be skipped



    


