============
objects
============

Below are the definitions for objects that you may run into.

Cook
-------

The cook object represents your character in the game.
In contains information on position, held item, and score.

================ ================ ===========
Name              Type             Description
================ ================ ===========
held_item         Item             The item the cook is currently holding
score             int              The Score you are currently have
position          tuple            The position your cook is currently in, (y,x)
================ ================ ===========

The cook starts in the middle of your kitchen.

Pizza
------

In the nation-state of Dominoes-TacoBell-Corpo-State, the only food allowed are pizza and tacos. A pizza can have the states rolled, sauced, 
and baked. Once it gets baked you can turn the pizza in to delivery station to gain points. The Cheese topping must be added to the Pizza to count.

Quality of Pizza
=================

Pizza quality is something that people care about, and sadly, if a quality of a pizza is not fit for human consumption, you are unlikely 
to receive repeating customers. The quality float of a pizza can be from 1.0 to 0.0 and uses the formula 

**score += (base + sum(toppings))* quality**


Instance Variables
===================

Instance variables for the Pizza object

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 state              PizzaState enums            An enum that describes what type of state the pizza is in
 __topping          ToppingType enums           An enum that describes the topping on the pizza there can only be a maximum of 3 topping per pizza with the first topping is cheese and it required.
================  =========================== ===================

Topping
---------

Toppings can be placed onto a pizza after they've been cut. 

Instance Variables
===================

Instance variables for the Topping object

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 Topping_type       ToppingType enums           An enum that describes what type of topping this is
 is_cut             bool                        Whether the topping is alreadly cut or not
================  =========================== ===================

Item
------

Important information
======================

Item this is the parent class for pizza and topping.

Instance Variables
===================

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 worth             int                         How many point is it worth
 quality           float                       The quality of the item currently
================  =========================== ===================