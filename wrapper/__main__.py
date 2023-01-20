import sys
import subprocess
import os

from game.engine import Engine
from game.utils.generate_game import generate
import game.config
import argparse

if __name__ == '__main__':
    # Setup Primary Parser
    par = argparse.ArgumentParser()

    # Create Subparsers
    spar = par.add_subparsers(title="Commands", dest="command")

    # Generate Subparser
    gen_subpar = spar.add_parser('generate', aliases=['g'], help='Generates a new random game map')
    
    # Run Subparser and optionals
    run_subpar = spar.add_parser('run', aliases=['r'],
                                 help='Runs your bot against the last generated map! "r -h" shows more options')
    
    # Visualize Subparser and optionals
    vis_subpar = spar.add_parser('visualize', aliases=['v'],
                                 help='Visualizes your bot against the last set of game logs! "v -h" shows more options')

    run_subpar.add_argument('-debug', '-d', action='store', type=int, nargs='?', const=-1, 
                            default=None, dest='debug', help='Allows for debugging when running your code')
    
    run_subpar.add_argument('-quiet', '-q', action='store_true', default=False,
                            dest='q_bool', help='Runs your AI... quietly :)')

    # Parse Command Line
    par_args = par.parse_args()
    
    # Main Action variable
    action = par_args.command

    # Generate game options
    if action in ['generate', 'g']:
        generate()
    
    # Run game options
    elif action in ['run', 'r']:
        # Additional args
        quiet = False

        if par_args.debug is not None:
            if par_args.debug >= 0:
                game.config.Debug.level = par_args.debug
            else:
                print('Valid debug input not found, using default value')
        
        if par_args.q_bool:
            quiet = True

        engine = Engine(quiet)
        engine.loop()

    # Run visualizer
    elif action in ['visualize', 'v']:
        # Get path to launcher
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Get path right above launcher
        dir_path = os.path.dirname(dir_path)
        # Go into Visualizer folder and get needed paths
        vis_path = os.path.join(dir_path, "Visualiser")
        # Run the logs adaption
        subprocess.run(["python" , "undercooked_adapter.py", "../logs/", "graphical.json"], cwd=vis_path)
        # Open the graphical log with Bytiser
        subprocess.run(["python", "bytiser.py", "config.json", "graphical.json"], cwd=vis_path)

    # Print help if no arguments are passed
    if len(sys.argv) == 1:
        print("\nLooks like you didn't tell the launcher what to do!"
              + "\nHere's the basic commands in case you've forgotten.\n")
        par.print_help()
