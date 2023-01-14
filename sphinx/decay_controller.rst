==========
Decay Controller
==========
The items held by the player have a decay rate for each item and once the item is decay too much is not useable.
The infestation event speed up decay on everything, but what the cook is holding.

Instance Variables
---------------------

Instance variables for the Gun object

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 Topping_type       ToppingType enums           An enum that describes what type of topping this is
 is_cut             bool                        Whether the topping is alreadly cut or not
================  =========================== ===================

Gun type enum
---------------

The following are the enums described above

================  =========================== 
 Topping Type              number            
================  =========================== 
   none             0
   dough            1
   cheese           2
   pepperoni        3
   sausage          4
   canadian_ham     5
   mushrooms        6
   peppers          7
   chicken          8
   olives           9
   anchovies        10
================  =========================== 

Gun stats
----------

Below are the point gain from adding this topping to the pizza

Topping point
==============

================  ========== ========================================================= 
 Topping           point       Information   
================  ========== ========================================================= 
 dough              50          Dough score used as base pizza score and required           
 cheese             20          Cheese is required and is the first topping of pizza
 pepperoni          40          n/a             
 sausage            40          n/a     
 canadian_ham       40          n/a
 mushrooms          40          n/a
 peppers            50          n/a
 chicken            40          n/a
 olives             50          n/a
 anchovies          50          n/a      
================  ========== =========================================================   
 