import pygame
import random

#constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize pygame
pygame.init()

# load and transform the background image
background_image = pygame.transform.scale(pygame.image.load
(r"C:\Users\sensw\OneDrive\Desktop\Codingal\sprite collision\space.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font once at the begining 
font = pygame.font.SysFont("Times new Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dodgerblue')) # background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width,height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        

# setup
screen = pygame.display.set_mode()
        
        














