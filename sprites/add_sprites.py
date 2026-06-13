import pygame
import random

# initialize pygame
pygame.init()

#custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# define basic colors using pygame.Color
# Background colors
BLUE = pygame.color('blue')
LIGHTBLUE = pygame.color('lightblue')
DARKBLUE = pygame.color('darkblue')

# Sprite colors
YELLOW = pygame.color('yellow')
MAGENTA = pygame.color('magenta')
ORANGE = pygame.color('orange')
WHITE = pygame.color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

    # constructor method
    def __init__(self, color, height, width):
        # call to the parent class (Sprite) constructor
        super().__init__()
        # Create the sprite's surface with dimensions and color
        self.image = pygame.Surface([width, height])
        self.immage.fill(color)
        #