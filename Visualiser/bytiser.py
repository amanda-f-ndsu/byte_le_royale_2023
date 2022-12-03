import pygame
from pygame.locals import *
import json

class BSprite(pygame.sprite.Sprite):
    def __init__(self, size, pos, image, scale):
        super(BSprite, self).__init__()
        self.surf = pygame.Surface((size[0], size[1]))
        self.surf.fill((0, 200, 255))
        self.surf.blit(image, (0,0), (pos[0], pos[1], image.get_height(), image.get_width()))
        self.rect = self.surf.get_rect()
        # Rescale
        self.surf = pygame.transform.scale(self.surf, (size[0] * scale, size[1] * scale))

class BLayer():
    def __init__(self, name, z_index):
        self.name = name
        self.z_index = z_index
        self.tiles = [] 



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

    def load_sprite(self, xIndex, yIndex):
        x = (xIndex * self.config["tile_size"][0]) + (xIndex * self.config["tile_spacing"][0]) + self.config["border_spacing"][0]
        y = (yIndex * self.config["tile_size"][1]) + (yIndex * self.config["tile_spacing"][1]) + self.config["border_spacing"][1]
        return BSprite(self.config["tile_size"], (x, y), self.tilemap, self.config["scale"])

    def get_sprite(self, key):
        # Check if valid key, if not, return the fallback sprite
        if key in self.config["keys"]:
            return self.load_sprite(self.config["keys"][key][0], self.config["keys"][key][1])
        else:
            return self.load_sprite(self.config["fallback"][0], self.config["fallback"][1])
        


    # Will visualize a log file
    def run_log(self, log_path):
        self.game_run = True

        # Testing setup
        floorSprite = self.get_sprite("floor")
        leftSprite = self.get_sprite("left_wall")
        rightSprite = self.get_sprite("right_wall")
        testLayer = BLayer("map", 0)
        testLayer.tiles = [
            [floorSprite, floorSprite, floorSprite],
            [leftSprite, floorSprite, rightSprite],
            [floorSprite, floorSprite, floorSprite]
        ]

        while self.game_run:
            # Clear screen
            self.screen.fill(self.black)
            # Check the event queue
            for event in pygame.event.get():
                # Check if a key was pressed
                if event.type == KEYDOWN:
                    # Check for exit key
                    if event.key == K_BACKSPACE:
                        self.game_run = False
                # Check for app quit
                elif event.type == QUIT:
                    self.game_run = False
            
            # Run current turn commands

            # Display layers
            self.draw_layer(testLayer)

            # Update display and wait for frames per second calc
            pygame.display.flip()
            self.clock.tick(self.config["fps"])

    # Parse a command item
    def parse_command(self, command):
        print(command)

    def draw_layer(self, layer: BLayer):
        print(layer.tiles)
        for y, y_item in enumerate(layer.tiles):
            print(y_item)
            for x, x_item in enumerate(y_item):
                self.screen.blit(x_item.surf, (x*self.config["scale"], y*self.config["scale"]))

    def update(self):
        pass

if(__name__ == "__main__"):
    bytiser = Bytiser("./config.json")
    bytiser.run_log("doesn't matter yet")