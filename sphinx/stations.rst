==========
Stations
==========

Station
--------

Important information
======================

Their are multiple stations with different functions. These stations help you transform the homely dough item into
a fully fledged pizza. Note that this is the parent class for the other stations.

Instance Variables
===================

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
Item               An Item object or None      A topping the station holds
is_infested        bool                        if true, the item held will decay faster
================  =========================== ===================

methods
=========

To interact with a station, simply set your chosen action to the interact action while standing infront of it


.. code-block:: python

    action.chosen_action = ActionType.interact

Dispenser
----------

Important information
======================

The dispenser dispenses Toppings. You can take a topping by calling the interact action near a dispenser. The items that the dispenser
holds will refresh in a given interval. See :doc:`stats` for this interval

Bin
----

Important information
======================

The bin allow you throw way topping or pizza that have not expired. This is used when the AI want to get rid of it and does not
want to storage the item in the storage station.

Cutter
-------

Important information
======================

The cutter will cut an uncut topping and return it to you immediatly. All toppings must be cut before they can be placed on a pizza.

Storage
----------

Important information
======================

The storage allow you place an item inside to be use later on. The storage containers are outdated and it can only hold one item at a time.
Calling interact on the storage station while you're holding an item and the storage container has an item will cause the items to swap.


Roller
---------

Important information
======================

The roller allow you to roll down the dough, so it could later to be use for the sauce station. This rolling process converts your 
topping object witha toppingtype of dough into a pizza object. Roller is the only non state of the are contraption as it just the 
cook rolling the dough. The employees are so fast it only take them micro-seconds.

Sauce
-------

Important information
======================

The sauce station allow you place the sauce on a rolled out dough. It will be returned immediatly.

At this station the cooks simply pour the sauce on top of rolled dough as these cooks are master of pouring sauce evenly.
These pour so well due to going to PSU (Pizza State University).


Combiner
----------

Important information
======================

The combiner takes a rolled pizza object. After it has the pizza, you can add toppings by holding a cut topping and calling the interact
action infront of the combiner. Pizzas can have up to 3 toppings. Calling interact infront of the Combiner without an item will take the 
pizza off of it. The first topping must always be cheese.

This state of the art contraption was made by the amazing scientists at the highest "Pizza League" colleges throughout 
the Dominoes-TacoBell-Corpo-State. Instead of picking up items and placing them on pizzas, the combiner allows for an efficient way
to astrally project the idea of a topping onto a pizza by using life energy from the companies very willing and consentual employees. 
Willing employees *(for a 5% discount on purchases from Pizza World franchises)* sit in a booth overnight and are sucked of life energy to fuel the 
super duper combiner. 


Oven
------

Important information
======================

The oven will cook a pizza object that has PizzaState.sauced and at least one topping. Calling interact with a pizza of this state
will place it in the oven and begin cooking it. Calling interact again when the pizza reaches it's baked state will remove the pizza from 
the oven. See :doc:`stats` for how many turns the pizza needs to bake.


Instance Variables
===================

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 is_powered         Boolean                     True if the oven has power
 is_active          Boolean                     True if there is a pizza cooking in there
 timer              int                         How many turns the pizza needs to cook
================  =========================== ===================


Delivery
---------

Important information
=======================

Turn in a baked pizza at this station.