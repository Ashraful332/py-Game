import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing a Line in Pygame")

# Define colors
WHITE = (255, 205, 255)
BLACK = (0, 5, 0)
RED = (255, 0, 25)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red line from (100, 100) to (700, 500) with a width of 5 pixels
    pygame.draw.line(screen, RED, (100, 100), (700, 500), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()