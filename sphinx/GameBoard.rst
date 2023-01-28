======================
The Game Board
======================

General Layout
-----------------

The map is a grid with two players that are separated by their side. The Combiner, Cutter, Oven, Roller, Sauce that are randomly place 
on the top and bottom row on the map. The player has to program their AI to go any station that they need. 

Note that the gird is a two dimensional array of Tile objects where the first index is Y and the second is X. So in your client

.. code-block:: python

   world.game_map[y][x]

Tile
------

Important information
======================

Tiles are an object that make up the gameboard two dimensional array.

Instance Variables
===================

Instance variables for the Tile object

================  =========================== ===================
 Name              Type                        Description
================  =========================== ===================
 is_wet_tile       bool                        Determines whether the tile is wet or not
 occupied_by       GameObject                  The object that occupies the tile
================  =========================== ===================


Counter
--------

Important information
======================

Counters seperate the cooks in the kitchen. This is to create two kitchens, in order to prevent the "Too many cooks" problem.

You do not recognize the tiles in the kitchen. Due to this, it is imperative that all cooks accessing this file be certified as
having a Cognitive Resistance Value (CRV) of no less than 14.5. Should you fail an automated CRV verification, please remain calm 
and do not move. A member of your resturaunt's medical staff will be with you shortly.

The counters are not useable and do not need to be considerd at all, do not bother interacting with them. You do not recognize the tiles.
The tiles never existed.