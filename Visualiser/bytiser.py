import pygame
from pygame.locals import *
import json

# Sprite Class that will load a sprite from a tile map passed as an image
class BSprite(pygame.sprite.Sprite):
    def __init__(self, size, pos, image, scale):
        super(BSprite, self).__init__()
        self.surf = pygame.Surface((size[0], size[1]))
        self.surf.fill((0, 200, 255))
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
    # Colors
    black = (0,0,0)
    white = (255, 255, 255)

    # Init object with a config path
    # Will set up pygame and check config
    def __init__(self, config_path):
        # Load config
        config_file = open(config_path)
        self.config = json.loads(config_file.read())
        # Load tilemap
        self.tilemap = pygame.image.load(self.config["tile_map"])
        
        # Init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]))
        # Clock for frames per second
        self.clock = pygame.time.Clock()
        # Init layer model
        self.layers = []

    # Load a sprite from the tile map
    def load_sprite(self, xIndex, yIndex):
        # Get the x and y pixel position of the sprite
        x = (xIndex * self.config["tile_size"][0]) + (xIndex * self.config["tile_spacing"][0]) + self.config["border_spacing"][0]
        y = (yIndex * self.config["tile_size"][1]) + (yIndex * self.config["tile_spacing"][1]) + self.config["border_spacing"][1]
        # Use the BSprite class to load from the tile map and scale it
        return BSprite(self.config["tile_size"], (x, y), self.tilemap, self.config["scale"])

    # Use a sprite key to find the relative position and then use load_sprite to get the BSprite
    # Will use a fallback sprite if the sprite key is invalid
    def get_sprite(self, key):
        # Check if valid key, if not, return the fallback sprite
        if key in self.config["keys"]:
            return self.load_sprite(self.config["keys"][key][0], self.config["keys"][key][1])
        else:
            return self.load_sprite(self.config["fallback"][0], self.config["fallback"][1])
        


    # Will visualize a log file
    def run_log(self, log_path):
        # Load the commands from the log file
        commands = json.loads(open(log_path).read())["log"]

        # Init function scope variables to track log progress
        game_run = True
        turn = 0
        index = 0
        # While game_run ie display should be running
        while game_run:
            # Clear screen
            self.screen.fill(self.black)
            # Check the event queue
            for event in pygame.event.get():
                # Check if a key was pressed
                if event.type == KEYDOWN:
                    # Check for exit key
                    if event.key == K_BACKSPACE:
                        game_run = False
                # Check for app quit
                elif event.type == QUIT:
                    game_run = False
            
            # Run current turn commands and increment the index
            # Pass the current command and parameters to parse_command
            # If we have reached the end of the file, stop incrementing and just skip to drawing layers
            while index < len(commands) and commands[index]["turn"] <= turn:
                self.parse_command(commands[index]["command"], commands[index]["value"])
                index += 1

            # Draw the layers in order of their z_index
            self.draw_layers()

            # Update display and wait for frames per second calc
            pygame.display.flip()
            self.clock.tick(self.config["fps"])
            # Make sure we are not going past the amount of turns in the log file
            if index < len(commands):
                turn += 1

    # Parse a command and its parameters
    def parse_command(self, command, value):
        print(str(command) + ": " + str(value))
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
                        layer.tiles[tile[1]][tile[0]] =  self.get_sprite(tile[2])
                # If there is a default tile, update all None spots with the default tile
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
                    self.screen.blit(layer.tiles[y][x].surf, (x*self.config["scale"] * self.config["tile_size"][0], y*self.config["scale"] * self.config["tile_size"][1]))
    
    # Draw all layers by assuming the layers are ordered by their z_index low to high
    # Every time a layer is added or deleted, the layer list is reordered so we can assume the layers are ordered correctly
    def draw_layers(self):
        for layer in self.layers:
            self.draw_layer(layer)

if(__name__ == "__main__"):
    bytiser = Bytiser("./config.json")
    bytiser.run_log("./test_log.json")