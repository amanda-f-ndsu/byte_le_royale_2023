=========
Cook
=========
The cook object represents your character in the game.
In contains information on position, held item, and score.

================ ================ ===========
Name              Type             Description
================ ================ ===========
held_item         Topping enums    The Topping the cook is currently holding
score             int              The Score you are currently have
position          tuple            The position your cook is currently in
================ ================ ===========

The cook start at the middle of kitchen

What your player can see their location
---------------------------
When you use the position in the cook class it will give your character current position.

.. code-block:: python

    cook.position


held item
---------

The player held item none or one topping type that the cook currently have.

Score
--------

The score method will hold the current the cooks have alreadly gotten.