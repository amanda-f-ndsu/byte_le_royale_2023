================
Getting Started
================

Goal
---------

The goal of this game is to win games against opponents. You do this by scoring more points than your opponent. The player who wins the most
games against other players in a "group run" after the competition has ended will win the competition.

More specifically, this game is about making pizzas


Running the game
-----------------

Python version
===============

Make sure to uninstall the visual studio version of python if you have visual studio installed. 
You can do this by re-running the installer and unselecting the python development kit then clicking update.

We recommend running a python version between 3.10 and 3.11

You can use any text editor for this competition, but we recommend visual studio code.

Getting the code
==================

Please download all of the assets you need from https://drive.google.com/drive/folders/1eC-kjPyY-Z7ZZYpovCg8WJvAwfnGAZbp?usp=sharing

This drive will contain the launcher.pyz file, two base clients, the visualizer and the requirements.txt

Submitting Issues
==================

If you run into issues with the game, please submit an issue to the discord in the bugs channel

Release of top clients
=======================

The top three clients at the end of the competition will be made public ( with censorship at the board's discretion (Association for Censorship Mmmmmmmmmmmmm))


Running the launcher
----------------------

NOTE: There are some packages requires for running this year's game. You can run the command 

.. code-block:: console

    python -m pip install -r requirements.txt

(To view the packages to be installed, simply open the requirements.txt file)

If you have problems installing the pygame package, try running the command


.. code-block:: console

    python -m pip install pygame --pre


Generating the map
==================

You can generate a new game map by calling

.. code-block:: python

    python launcher.pyz g

within a terminal in the byte-le folder. You can keep the same game map by just not running the above command.
With the same map and same clients, the end results should be the same.


Running the game
=================

You can run the bot by calling

.. code-block:: python

    python launcher.pyz r

within the terminal. Print statements within your client will print if you wish to use them for debugging purposes. Alternatively, you can view
the turn logs that are produced within the logs folder.


Running the visualizer
=======================

As a third option for debugging, we have built a visualizer! The visualizer visually depicts the logs that are produced, so you can more easily decipher what went wrong. 
The visualizer can be run with

.. code-block:: python

    python launcher.pyz v

See :doc:`visualizer` for more commands


Improving the bot
-----------------

All improvements should be made within the client. We provide a base client but you are welcome to rename the file or create multiple client files. 
Note that if you make multiple files, there can only be two client in the root folder. Place the other clients in the test_clients folder. Make sure to check the
documentation for hints on how to improve!

Cook options during turns
==========================

Each turn, a cook can do one of two things. You can choose to move the cook or choose if you want to interact with an adjacent station 
in that order. See :doc:`action` and :doc:`stations`

Other Logic
============

After the cook has been given the chance to move and interact, dispensers may dispense a new topping and ovens will cook a pizza for 
another turn. After this, event logic will take place. This means that a new event will start if one is meant to start during that turn.
Events can be seen at :doc:`events` and stats at :doc:`stats`


Scrimmage!
-----------

The actual competition occurs on the server! View the :doc:`server` documentation for more info.

