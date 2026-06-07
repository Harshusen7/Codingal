import pygame

# initialize pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HIEGHT = 500,500

# initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
pygame.display.set_caption('Adding image and background image')

#load and scale images directly
background_image = pygame.transform.scale(



)

object_image = pygame.transform.scale(


)
object_rect = object_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HIEGHT /// 2  - 30)
)

# Initialize font

