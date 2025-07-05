import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Impress Game")

# Load images
background_image = pygame.image.load("IMG_0531.jpg")
player_image = pygame.image.load("PrithviRaj.png")

# Set player position
player_pos = [window_size[0] // 2, window_size[1] - player_image.get_height()]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Update player position based on mouse position
    player_pos[0] = mouse_pos[0] - player_image.get_width() // 2

    # Draw the player
    screen.blit(player_image, player_pos)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
