import pygame, sys # imports pygame and sys modules. Graphics, sound, and other features that Pygame provides are in the pygame module
from pygame.locals import * # imports everything from pygame

FPS = 60 # define game FPS
fpsClock = pygame.time.Clock()

pygame.init() # initialize pygame
GAME_WIDTH = 1250
GAME_HEIGHT = 900
GAME_SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) # set display window
pygame.display.set_caption('New Game') # set game title

RED = (255, 0, 0) # max is 255
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

playerpaddlewidth = 30
playerpaddleheight = 170
BALL_SIZE = 30

class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.up = False
        self.down = False
        self.speed = 10
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(GAME_SCREEN, self.color, (self.x, self.y, self.width, self.height)) # x, y, width, height

    def move(self):
        if self.up == True and self.y > 0:
            self.y -= self.speed
        if self.down == True and self.y + self.height < 900:
            self.y += self.speed

class Ball():
    BALL_SPEED = 8
    def __init__ (self, x, y, size, color):
        self.x = x
        self.y = y
        self.color = color
        self.x_vel = self.BALL_SPEED
        self.y_vel = 0
        self.width = size
        self.height = size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(GAME_SCREEN, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


player1 = Block(20, GAME_HEIGHT // 2 - playerpaddleheight // 2 , playerpaddlewidth, playerpaddleheight, WHITE)
player2 = Block (GAME_WIDTH - 20 - playerpaddlewidth, GAME_HEIGHT // 2 - playerpaddleheight // 2, playerpaddlewidth ,playerpaddleheight, GREEN)

ball = Ball(GAME_WIDTH//2 - BALL_SIZE//2, GAME_HEIGHT//2  - BALL_SIZE//2, BALL_SIZE, BLUE)

while True: # main game loop
    GAME_SCREEN.fill(BLACK)
    
    player1.draw()
    player1.move()

    player2.draw()
    player2.move()

    ball.draw()
    ball.move()

    # handle_collision(ball, player1, player2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # player controls go below here...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.up = True
            if event.key == pygame.K_s:
                player1.down = True
            if event.key == pygame.K_UP:
                player2.up = True
            if event.key == pygame.K_DOWN:
                player2.down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.up = False 
            if event.key == pygame.K_s:
                player1.down = False 
            if event.key == pygame.K_UP:
                player2.up = False
            if event.key == pygame.K_DOWN:
                player2.down = False

            
    pygame.display.update()
    fpsClock.tick(FPS)