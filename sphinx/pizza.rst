==========
Pizza
==========
The pizza is the food that the cook are making. The cook have multiple stage include  rolled, sauced, and baked. Once it get baked turn the pizza in to delivery point to gain point.
Cheese topping must be added to the Pizza to count.

Instance Variables
---------------------

Instance variables for the Pizza object

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 state              PizzaState enums            An enum that describes what type of state the pizza is in
 __topping          PizzaState enums            An enum that describes the topping on the pizza there can only be a maximum of 3 topping per pizza with the first topping is cheese and it required.
================  =========================== ===================

Pizza State enum
---------------

The following are the enums described above

================  =========================== 
 Pizza State          number            
================  =========================== 
   none              0
   rolled            1
   sauced            2
   baked             3
================  =========================== 