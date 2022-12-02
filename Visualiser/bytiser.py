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


class Bytiser():
    # Colors
    black = (0,0,0)
    white = (255, 255, 255)

    # Init object with a config path
    # Will set up pygame and check config
    def __init__(self, configPath):
        # Load config
        configFile = open(configPath)
        self.config = json.loads(configFile.read())
        # Load tilemap
        self.tilemap = pygame.image.load(self.config["tile_map"])
        
        # Init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.config["screen_width"], self.config["screen_height"]))
        # Clock for frames per second
        self.clock = pygame.time.Clock()

    def get_sprite(self, xIndex, yIndex):
        x = (xIndex * self.config["tile_size"][0]) + (xIndex * self.config["tile_spacing"][0]) + self.config["border_spacing"][0]
        y = (yIndex * self.config["tile_size"][1]) + (yIndex * self.config["tile_spacing"][1]) + self.config["border_spacing"][1]
        return BSprite(self.config["tile_size"], (x, y), self.tilemap, self.config["scale"])

    # Will visualize a log file
    def run_log(self, logPath):
        self.gameRun = True

        # Try creating a sprite from the tilemap
        guy = self.get_sprite(4, 0)

        while self.gameRun:
            # Clear screen
            self.screen.fill(self.black)
            # Check the event queue
            for event in pygame.event.get():
                # Check if a key was pressed
                if event.type == KEYDOWN:
                    # Check for exit key
                    if event.key == K_BACKSPACE:
                        self.gameRun = False
                # Check for app quit
                elif event.type == QUIT:
                    self.gameRun = False
            
            self.screen.blit(guy.surf, (100, 100))
            self.screen.blit(self.tilemap, (500,500))

            # Update display and wait for frames per second calc
            pygame.display.flip()
            self.clock.tick(self.config["fps"])


    def update(self):
        pass

if(__name__ == "__main__"):
    bytiser = Bytiser("./config.json")
    bytiser.run_log("doesn't matter yet")