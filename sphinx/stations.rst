==========
Stations
==========

Station
========

Important information
------------------------
Their are multiple stations with different functions. These stations help you transform the homely dough item into
a fully fledged pizza. Note that this is the parent class for the other stations

Instance Variables
------------------

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
Item               An Item object or None       A topping that are store in the storage
is_infested        bool                        if true topping decay faster
================  =========================== ===================

methods
--------

To interact with a station, simply call the interact action while standing infront of it


Storage
==========

Important information
------------------------
The storage allow you place an item inside to be use later on. 
The storage containers are outdated and it can only hold one item at a time.



Roller
==========

Important information
------------------------
The roller allow you to roll down the dough, so it could later to be use for the sauce station.
Roller is the only non state of the are contraption as it just the cook rolling the dough that it. 
The employees are so fast it only take them micro-seconds

Oven
==========

Important information
------------------------
The oven allow you place a pizza onto the oven then  pizza get cook the chef will need to come in time or else it will get burnt.
This state of the art contraption was made by the amazing scientists at the highest "Pizza League" colleges throughout the nations. Instead of picking up items and placing them
on pizzas, the combiner allows for an efficient way to astrally project the idea of a topping onto a pizza by using life energy from the companies very willing and consentual employees.
Willing employees (for a 5% discount on purchases from Pizza World franchises) sit in a booth overnight and are sucked of life energy to fuel the super duper combiner. 


Instance Variables
------------------

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
Item               PizzaState enums            The Pizza that you are adding topping to
================  =========================== ===================


Dispenser
==========

Important information
------------------------
The dispenser display topping every once and while so the cook can grab it and use it on the pizza
dispenser is the beginning point where you get all topping and dough
This is a state of the art contraption that will grab the the topping in the backroom and display to the cooks.

Instance Variables
------------------

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
Item               Topping enums               Topping that is display to cooks for them to take it
================  =========================== ===================

Cutter
==========

Important information
------------------------
The cutter allow the cook to bring an topping to the cutter where topping get cut the into slice to be use for pizza.

Sauce
==========

Important information
------------------------
The sauce station allow you place the sauce on a rolled out dough.
This station the cooks simply pour the sauce on top of rolled dough as these cooks are master of pouring sauce evenly.
These pour so well due to going to Pizza State University.





