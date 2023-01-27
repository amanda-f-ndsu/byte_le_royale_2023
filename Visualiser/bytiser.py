import pygame
from pygame.locals import *
import json
import sys
from PIL import Image
import cv2
import numpy
import math

# Sprite Class that will load a sprite from a tile map passed as an image
class BSprite(pygame.sprite.Sprite):
    def __init__(self, size, pos, image, scale):
        super(BSprite, self).__init__()
        # Create a new surface with the ability to have an alpha channel
        self.surf = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
        # Clear the surface, make it fully transparent
        self.surf.fill((0, 0, 0, 0))
        # Blit a crop of our loaded image onto our sprite
        self.surf.blit(image, (0,0), (pos[0], pos[1], image.get_height(), image.get_width()))
        self.rect = self.surf.get_rect()
        # Rescale
        self.surf = pygame.transform.scale(self.surf, (size[0] * scale, size[1] * scale))

# Layer Structure with name, width, and height
# Layers are drawn based on their z_index, low to high
class BLayer():
    def __init__(self, name, z_index, width, height):
        self.name = name
        self.z_index = z_index
        self.width = width
        self.height = height
        self.tiles = []
        self.clear()

    def clear(self):
        self.tiles = []
        for y in range(self.height):
            self.tiles.append([])
            for x in range(self.width):
                self.tiles[y].append(None)

# Main Logic class
# Init with a config file then use run_log with a log file to visualize
class Bytiser():
    # Quick Colors
    black = (0,0,0)
    white = (255, 255, 255)
    clear = (0, 0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    debug_color = blue # Color of debug text if shown

    # Init object with a config path
    # Will set up pygame and check config
    def __init__(self, config_path, paused = True):
        # Load config
        config_file = open(config_path)
        self.config = json.loads(config_file.read())
        self.paused = paused
        self.quits = not paused
        # Init pygame
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]))
        # Load tile map images
        self.tile_maps = {}
        for key in self.config["tile_maps"]:
            self.tile_maps[key] = pygame.image.load(self.config["tile_maps"][key]["source"])
            self.tile_maps[key] = self.tile_maps[key].convert_alpha()
        # Clock for frames per second
        self.clock = pygame.time.Clock()
        # Init layer model
        self.layers = []
        # Load font
        self.font = pygame.font.SysFont(self.config["font"], self.config["font_size"])
        # Init score dict
        self.scores = {}
        self.debug = True
        self.text_layer = pygame.Surface((self.config["screen_width"], self.config["screen_height"]), pygame.SRCALPHA)

    # Load a sprite from the tile map
    def load_sprite(self, tile_map_key, xIndex, yIndex):
        # Get the x and y pixel position of the sprite
        x = (xIndex * self.config["tile_maps"][tile_map_key]["tile_size"][0]) + (xIndex * self.config["tile_maps"][tile_map_key]["tile_spacing"][0]) + self.config["tile_maps"][tile_map_key]["border_spacing"][0]
        y = (yIndex * self.config["tile_maps"][tile_map_key]["tile_size"][1]) + (yIndex * self.config["tile_maps"][tile_map_key]["tile_spacing"][1]) + self.config["tile_maps"][tile_map_key]["border_spacing"][1]
        # Find the adjustment scale to make the tile load to the same tile size as global config
        adjustment = self.config["global_tile_size"][0] / self.config["tile_maps"][tile_map_key]["tile_size"][0]
        # Use the BSprite class to load from the tile map
        return BSprite(self.config["tile_maps"][tile_map_key]["tile_size"], (x, y), self.tile_maps[tile_map_key], self.config["scale"] * adjustment)

    # Use a sprite key to find the relative position and then use load_sprite to get the BSprite
    # Will use a fallback sprite if the sprite key is invalid
    def get_sprite(self, key):
        # Check if valid key, if not, return the fallback sprite
        if key == None:
            return None
        if key in self.config["keys"]:
            return self.load_sprite(self.config["keys"][key][0], self.config["keys"][key][1], self.config["keys"][key][2])
        else:
            return self.load_sprite(self.config["fallback"][0], self.config["fallback"][1], self.config["fallback"][2])

    # Will visualize a log file
    def run_log(self, log_path):
        # Load the commands from the log file
        self.commands = json.loads(open(log_path).read())["log"]

        # Init function scope variables to track log progress
        game_run = True
        self.speed = 0
        self.turn = 0
        self.index = 0
        self.shift = False
        # Clear screen
        self.screen.fill(self.black)
        # While game_run ie display should be running
        while game_run:
            # Check the event queue
            for event in pygame.event.get():
                # Check if a key was pressed
                if event.type == KEYDOWN:
                    # Check for exit key
                    if event.key == K_BACKSPACE:
                        game_run = False
                    # Check for forward turn
                    elif event.key == K_RIGHT:
                        if self.shift and self.index+10 < len(self.commands):
                            self.turn += 9
                            self.go_to_turn(self.turn)
                        else:
                            self.next_turn()
                    # Check for backward turn
                    # Also make sure the current turn is not 0
                    elif event.key == K_LEFT and self.turn > 1:
                        # Check if shift key is pressed
                        if self.shift and self.index+10 < len(self.commands):
                            self.turn -= 11
                        else:
                            # If not at the end, sub 2 because self.turn is actually the number of the next turn to display
                            if self.index < len(self.commands):
                                self.turn -= 2
                            # If we are at the end, then self.turn is capped at the end turn so only sub 1
                            else:
                                self.turn -= 1
                        self.go_to_turn(self.turn)
                    elif event.key == K_SPACE:
                        self.paused = not self.paused
                    elif event.key == K_UP:
                        self.speed += 1
                    elif event.key == K_DOWN:
                        self.speed -= 1
                    elif event.key == K_d:
                        # Show debug info on d press
                        self.debug = not self.debug
                    elif event.key == K_r:
                        # Restart log on r press
                        self.paused = True
                        self.speed = 0
                        self.turn = 0
                        self.index = 0
                        # Clear screen
                        self.screen.fill(self.black)
                        # Go to next turn to make sure screen is updated
                        self.next_turn()
                    elif event.key == K_LSHIFT:
                        self.shift = True
                    elif event.key == K_s:
                        if self.shift:
                            self.save_video()
                        else:
                            self.save_gif()
                elif event.type == KEYUP:
                    if event.key == K_UP:
                        self.speed -= 1
                    elif event.key == K_DOWN:
                        self.speed += 1
                    elif event.key == K_LSHIFT:
                        self.shift = False
                # Check for app quit
                elif event.type == QUIT:
                    game_run = False
            # If not paused, default to going to the next turn
            if not self.paused:
                self.next_turn()
            # Check if at end of commands, if so then pause
            if self.index >= len(self.commands):
                self.paused = True
                # If we want to quit at the end of play, then mark game end
                if self.quits:
                    game_run = False

            # Frames per second based on up and down arrows
            if self.speed == 1:
                self.clock.tick(self.config["fps"] * 2)
            elif self.speed == -1:
                self.clock.tick(self.config["fps"] / 2)
            else:
                self.clock.tick(self.config["fps"])      

    def save_gif(self):
        images = []
        self.turn = 0
        self.index = 0
        width = self.config["screen_width"]
        height = self.config["screen_height"]
        while self.index < len(self.commands):
            new_image = pygame.image.tostring(self.screen.copy(), "RGBA", False)
            new_image = Image.frombytes("RGBA", (width, height), new_image)
            # Scale image 
            new_image.thumbnail([400, 400])
            images.append(new_image)
            self.next_turn()
        images[0].save("./out.gif", append_images=images[1:], save_all=True, optimize=True, duration=10)
        print("Saved gif")

    def save_video(self):
        self.turn = 0
        self.index = 0
        size = (self.config["screen_width"], self.config["screen_height"])
        scaled = (math.ceil(size[0]/2), math.ceil(size[1]/2))
        writer = cv2.VideoWriter("out.mp4", cv2.VideoWriter_fourcc(*'H264'), 10, scaled)
        
        while self.index < len(self.commands):
            # Convert to PIL Image
            new_image = pygame.image.tostring(self.screen.copy(), "RGBA", False)
            new_image = Image.frombytes("RGBA", size, new_image)
            # Scale image 
            new_image.thumbnail(scaled)
            # Convert to OpenCV Image with numpty
            new_image = numpy.array(new_image)
            new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
            # Write image and go to next turn
            writer.write(new_image)
            self.next_turn()
        writer.release()
        print("Saved video")

    def next_turn(self):
        # Clear the screen
        self.screen.fill(self.black)
        # Run current turn commands and increment the index
        # Pass the current command and parameters to parse_command
        # If we have reached the end of the file, stop incrementing and just skip to drawing layers
        while self.index < len(self.commands) and self.commands[self.index]["turn"] <= self.turn:
            self.parse_command(self.commands[self.index]["command"], self.commands[self.index]["value"])
            self.index += 1

        # Draw the layers in order of their z_index
        self.draw_layers()

        # Draw the scores
        self.draw_scores()

        # Update display and wait for frames per second calc
        pygame.display.flip()
        # Make sure we are not going past the amount of turns in the log file
        if self.index < len(self.commands):
            self.turn += 1

    # Loop through all turns to get to the specific turn number
    def go_to_turn(self, num):
        self.turn = 0
        self.index = 0
        self.layers = []
        self.scores = {}

        # self.turn is supposed to be the number of the NEXT turn so use less than or equal
        while self.turn <= num:
            self.next_turn()

    # Parse a command and its parameters
    def parse_command(self, command, value):
        # Add a new layer and check the z_index ordering
        if command == "add_layer":
            new_layer = BLayer(value[0], value[1], value[2], value[3])
            self.layers.append(new_layer)
            self.reorder_layers()
        # Clear the layer and then update layer with tiles
        if command == "set_layer":
            for layer in self.layers:
                if layer.name == value[0]:
                    layer.clear()
            self.update_layer(value[0], value[1])
        # Update layer with tiles
        if command == "update_layer":
            self.update_layer(value[0], value[1])
        # Add score
        if command == "add_score":
            self.add_score(value[0], value[1], value[2], value[3])
        # Set score 
        if command == "set_score":
            # If the id is null, loop through all scores and set values
            if value[0] is None:
                for score in self.scores:
                    self.set_score(score, value[1], value[2], value[3])
            else:
                self.set_score(value[0], value[1], value[2], value[3])
            
        # Remove score
        if command == "remove_score":
            self.remove_score(value[0])

    # Reorder the layers by their z_index, from low to high
    def reorder_layers(self):
        temp_list = []

        # Get lowest z index
        while len(self.layers) > 0:
            low = None
            for layer in self.layers:
                if low == None or low.z_index > layer.z_index:
                    low = layer
            temp_list.append(low)
            self.layers.remove(low)

        # All layers are now ordered in temp_list in correct z_order
        self.layers = temp_list

    # Use the name and tiles to update a layer
    def update_layer(self, name, sets):
        # Check all layers for a name match
        for layer in self.layers:
            # Found a name match!
            if layer.name == name:
                default_tile = None # Default to None so it will be transparent
                for tile in sets:
                    # Check if making default tile
                    if(tile[0] == None and tile[1] == None):
                        default_tile = self.get_sprite(tile[2])
                    else:
                        # Get the BSprite based on the key and update the layer tile location
                        try:
                            layer.tiles[tile[1]][tile[0]] =  self.get_sprite(tile[2])
                        except:
                            breakpoint()
                            print()

                # If there is a default tiles, update all None spots with the default tile
                if default_tile != None:
                    for y in range(layer.height):
                        for x in range(layer.width):
                            if layer.tiles[y][x] == None:
                                layer.tiles[y][x] = default_tile

    # Draw one layer's tiles onto the screen surface
    def draw_layer(self, layer: BLayer):
        for y in range(layer.height):
            for x in range(layer.width):
                # Leave transparent if None
                if layer.tiles[y][x] is not None:
                    # Blit the sprite at the position adjusted by tile size and scale
                    self.screen.blit(layer.tiles[y][x].surf, (x*self.config["scale"] * self.config["global_tile_size"][0], y*self.config["scale"] * self.config["global_tile_size"][1]))
    
    # Draw all layers by assuming the layers are ordered by their z_index low to high
    # Every time a layer is added or deleted, the layer list is reordered so we can assume the layers are ordered correctly
    def draw_layers(self):
        for layer in self.layers:
            self.draw_layer(layer)
    
    # Draw all the score texts on top of the screen
    def draw_scores(self):
        # Clear text layer
        self.text_layer.fill(self.clear)
        # For each score, add it as text to the text_layer Surface
        for score in self.scores:
            score = self.scores[score]
            text = self.font.render(score[0] + str(score[1]), True, (self.config["font_color"][0], self.config["font_color"][1], self.config["font_color"][2]))
            self.text_layer.blit(text, (score[2][0], score[2][1]))
        # Check if we also want debug information to be added to the text layer
        if self.debug:
            output = "Turn: " + str(self.turn)
            if self.paused:
                output += " || Paused"
            else:
                output += " || Playing"
            if self.speed == 0:
                output += " || x1"
            elif self.speed == 1:
                output += " || x2"
            elif self.speed == -1:
                output += " || x0.5"
            text = self.font.render(output, True, self.debug_color)
            self.text_layer.blit(text, (10,10))
        # Add the text layer to the screen
        self.screen.blit(self.text_layer, (0, 0))
            

    # Add a score to the scores dictionary
    def add_score(self, id, text, value, pos):
        self.scores[id] = [text, value, pos]
    
    # Update a score from the scores dictionary
    # Null values keep the previous value
    def set_score(self, id, text, value, pos):
        # If the id doesn't exist, error and don't try and set
        if id not in self.scores:
            print("ERROR: Cannot set score where Score Id " + id + " doesn't exist!")
            return
        # Check for null overrides
        if text is None:
            text = self.scores[id][0]
        if value is None:
            value = self.scores[id][1]
        if pos is None:
            pos = self.scores[id][2]
        # Set full updated score
        self.scores[id] = [text, value, pos]

    # Remove a score from the scores dictionary based on id
    def remove_score(self, id):
        # Make sure the id is in the dictionary 
        if id not in self.scores:
            print("ERROR: Cannot remove score where Score Id " + id + " doesn't exist!")
        else:
            self.scores.pop(id)

# Run file as a command
def help():
    print("COMMAND USAGE for PYTHON 3")
    print("python ./bytiser.py configFile logFile")
    print("python ./bytiser.py --fonts <-- Will display list of system fonts available to pygame")
    print("Zero arguments will default to ./config.json and ./graphical.json")
    print("Controls:")
    print("Space - Pause/Play")
    print("Up/Down Arrow(hold) - Speed Up or Slow Down")
    print("Left/Right Arrow - Go forward/back one turn")
    print("d - Enable debug stats (go to next turn to update display)")
    print("r - Restart from beginning")
    print("left shift(hold) - Left/Right Arrow now does 10 turns instead of 1")
    print("s - Save run as gif to ./out.gif (optimised to ~6mb for discord)")
    print("left shift + s - Save run as mp4 to ./out.mp4 (optimised to ~7mb for discord, might not work on all platforms")
    
if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        bytiser = Bytiser("./config.json")
        bytiser.run_log("./graphical.json")
    elif (len(sys.argv) == 3):
        bytiser = Bytiser(sys.argv[1])
        bytiser.run_log(sys.argv[2])
    elif (len(sys.argv) == 4):
        bytiser = Bytiser(sys.argv[1], True if sys.argv[3] == "True" else False)
        bytiser.run_log(sys.argv[2])
    elif (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        help()
    elif (len(sys.argv) == 2 and sys.argv[1] == "--fonts"):
        print(pygame.font.get_fonts())
    else:
        help()
    