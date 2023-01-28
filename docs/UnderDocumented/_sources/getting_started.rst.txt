================
Getting Started
================

Goal
---------

The goal of this game is to win games against opponents. You do this by scoring more points than your opponent. The player who wins the most
games against other players in a "group run" after the competition has ended will win the competition.

More specifically, this game is about making pizzas

Cook options during turns
--------------------------

Each turn, a cook can do one of two things. You can choose to move the cook or choose if you want to interact with an adjacent station 
in that order. See :doc:`action` and :doc:`stations`

Other Logic
-------------

After the cook has been given the chance to move and interact, dispensers may dispense a new topping and ovens will cook a pizza for 
another turn. After this, event logic will take place. This means that a new event will start if one is meant to start during that turn.
Events can be seen at :doc:`events` and stats at :doc:`stats`