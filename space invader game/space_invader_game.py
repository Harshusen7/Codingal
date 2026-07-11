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
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# bullet
bulletImg = pygame.image.load(r" ")

bulletIng = pygame.transform.scale(bulletImg, (16, 24))
playerImg
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    # display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    # display the game over text
    over_text = over_font.render("GAMEOVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    # draw the player on the screen
    screen.blit(playerImg, (x,y))

def enemy(x, y, i):
    # draw an enemy on the screen
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    # Fire a bullet from the players position
    global bullet_state
    bullet_state = "fire" 
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # check if there is a collision between the enemy and the bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # player 
            
          
















                         
                         
    
    

    



