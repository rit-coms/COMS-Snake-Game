import pygame

# Initializes the pygame
pygame.init()

# creates the screen
screen = pygame.display.set_mode((800,550))

"""
Game Loop
If the game is closed the loop ends
"""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False