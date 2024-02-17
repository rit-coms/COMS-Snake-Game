import pygame
import sys
from pygame.math import Vector2
import random

class DUCK:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1, 0)
        self.new_duck = False

    def draw_duck(self):
        for index, block in enumerate(self.body):  # Use enumerate to get both index and block
            duck_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            if index == 0:  
                color = (55, 119, 32)   
            else:
                color = (222, 204, 48)  
            pygame.draw.rect(screen, color, duck_rect)

    """Makes a copy of the duck body and adds a block if there was a collision, otherwise moves head but removes tail"""
    def move_duck(self):
        if self.new_duck == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_duck = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    """Allows the duck body to have more ducks added to it"""
    def add_duck(self):
        self.new_duck = True

class BREAD:
    def __init__(self):
        self.randomize()

    """Creates a bread rectangle and draws it onto the screen"""
    def draw_bread(self):
        bread_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (192, 161, 59), bread_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.duck = DUCK()
        self.bread = BREAD()
    
    def update(self):
        self.duck.move_duck()
        self.check_collision()

    def draw_elements(self):
        self.bread.draw_bread()
        self.duck.draw_duck()

    def check_collision(self):
        if self.bread.pos == self.duck.body[0]:
            self.bread.randomize()
            self.duck.add_duck()


# Initializes pygame
pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

running = True
# Gameloop
while running:
    screen.fill((41, 180, 32))
    main_game.draw_elements()
    for event in pygame.event.get():
        # exits the game
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.duck.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.duck.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.duck.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.duck.direction = Vector2(1, 0)
    
    pygame.display.update()
    # Framerate
    clock.tick(60)