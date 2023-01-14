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

    actions.chosen_action(ActionType.interact) -> None

This will set your intent to interact with items on the map, including all station dispenser, storage, delivery, and bin.
Remember that ActionType.interact is an enum!
(So you need to make sure you leave in the import for enums in the given client)

Move
======

.. code-block:: python

    actions.chosen_action(ActionType.Move.up) -> None

.. code-block:: python

    actions.chosen_action(ActionType.Move.down) -> None

.. code-block:: python

    actions.chosen_action(ActionType.Move.left) -> None

.. code-block:: python

    actions.chosen_action(ActionType.Move.right) -> None

This will use your action to move around. It will allow the User to moved their AI up, down, left, and right.
