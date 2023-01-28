=====================
Taking Action
=====================

The Action Object
------------------

Taking actions is managed by an action object passed to the player each turn.
This comes in as "actions" in the take_turns() method in your client.

Available Actions
------------------

Each turn you can take one action.
If you take multiple actions your client will do the last one that is set.

Interact
========

.. code-block:: python

    actions.chosen_action = ActionType.interact 

This will set your intent to interact with stations on the map, see :doc:`stations`

Move
======

.. code-block:: python

    actions.chosen_action = ActionType.Move.up

.. code-block:: python

    actions.chosen_action = ActionType.Move.down

.. code-block:: python

    actions.chosen_action = ActionType.Move.left

.. code-block:: python

    actions.chosen_action = ActionType.Move.right

This will use your action to move around. It will allow the User to moved their AI up, down, left, and right.
