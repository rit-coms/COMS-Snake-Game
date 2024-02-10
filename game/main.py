import pygame

# Initializes the pygame
pygame.init()

# creates the screen
screen = pygame.display.set_mode((800, 550))

# Title and Icon
pygame.display.set_caption("Imprint")
icon = pygame.image.load("./game/assets/duck_icon.png")
pygame.display.set_icon(icon)

# Background 
#background = pygame.image.load("./game/assets/grass_background.png")

# Player 
playerImg = pygame.image.load("./game/assets/duck_player.png")
playerX = 370
playerY = 275
playerX_change = 0
playerY_change = 0

# Draws the player at the specific coordiante
def player(x:int , y:int):
    screen.blit(playerImg, (x, y))

"""
Game Loop
If the game is closed the loop ends
"""
running = True
while running:

    # updates screen background to green using RGB
    screen.fill((41, 180, 32))

    # background image
    #screen.blit(background, (0, 0))


    for event in pygame.event.get():
        # Allows the game to be closed
        if event.type == pygame.QUIT:
            running = False
    
        # Checks for keystroke 
        if event.type == pygame.KEYDOWN:
            # Note: Y postion or X position is set to 0 to zero inorder to restrict diagnol movement
            # Move left
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -0.1
                playerY_change = 0

            # Move right
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 0.1
                playerY_change = 0

            # Move up
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                playerY_change = -0.1
                playerX_change = 0

            # Move down
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                playerY_change = 0.1
                playerX_change = 0

        # Stops movement after key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                playerY_change = 0
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Changes the player's position
    playerX += playerX_change
    playerY += playerY_change

    # Sets the boder for the game, depends on player size (64px)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 486:
        playerY = 486

    player(playerX, playerY)
    # needed for continous updates to the game display
    pygame.display.update()