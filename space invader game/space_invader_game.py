import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background
background = pygame.image.load
(r"")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(r"")
icon = pygame.transform.scale(icon, (64,64))
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load(r"")
playerImg = pygame.transform.scale(playerImg, (64,64))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemy_image = pygame.image.load
    (r"")

    enemy_image = pygame.transform.scale(enemy_image, (64,64))

    enemyImg.append(enemy_image)
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY))

