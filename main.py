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

playerpaddlewidth = 60
playerpaddleheight = 200
BALL_SIZE = 30
WINNING_SCORE = 5


def draw_text(text, font_size, color, x, y):
	font = pygame.font.SysFont('freesansbold.ttf', font_size)
	img = font.render(text, True, color)
	GAME_SCREEN.blit(img, (x, y))

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
    BALL_SPEED = 13
    def __init__ (self, x, y, size, color):
        self.x = self.x_original = x
        self.y = self.y_original = y
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

    def reset(self):
        self.x = self.x_original
        self.y = self.y_original
        self.x_vel = self.BALL_SPEED
        self.y_vel = 0



# handle collision
def handle_collision(ball, left_paddle, right_paddle):
  # top and bottom wall collision
  if ball.y + BALL_SIZE >= GAME_HEIGHT: # bottom wall collision
    ball.y_vel *= -1
  if ball.y <= 0:
    ball.y_vel *= -1

  # paddle collision
  if ball.x_vel < 0: # if ball is moving to the left
    if ball.y >= (
        left_paddle.y - BALL_SIZE
    ) and ball.y <= left_paddle.y + left_paddle.height:
      if ball.x <= left_paddle.x + left_paddle.width:
        ball.x_vel *= -1

        middle_y = left_paddle.y + left_paddle.height // 2
        difference_in_y = middle_y - ball.y
        reduction_factor = (left_paddle.height // 2) // ball.BALL_SPEED
        y_vel = difference_in_y // reduction_factor
        ball.y_vel = -1 * y_vel
  else:
    if ball.y >= (
        right_paddle.y - BALL_SIZE
    ) and ball.y <= right_paddle.y + right_paddle.height:
      if ball.x + BALL_SIZE >= right_paddle.x:
        ball.x_vel *= -1

        middle_y = right_paddle.y + left_paddle.height // 2
        difference_in_y = middle_y - ball.y
        reduction_factor = (right_paddle.height // 2) // ball.BALL_SPEED
        y_vel = difference_in_y // reduction_factor
        ball.y_vel = -1 * y_vel


player1 = Block(20, GAME_HEIGHT // 2 - playerpaddleheight // 2 , playerpaddlewidth, playerpaddleheight, WHITE)
player2 = Block (GAME_WIDTH - 20 - playerpaddlewidth, GAME_HEIGHT // 2 - playerpaddleheight // 2, playerpaddlewidth ,playerpaddleheight, GREEN)

ball = Ball(GAME_WIDTH//2 - BALL_SIZE//2, GAME_HEIGHT//2  - BALL_SIZE//2, BALL_SIZE, BLUE)

player1score = 0
player2score = 0

game_over = False

while True: # main game loop
    GAME_SCREEN.fill(BLACK)
    
    player1.draw()
    player1.move()

    player2.draw()
    player2.move()

    ball.draw()
    ball.move()

    draw_text("player 1: " + str(player1score), 40, WHITE, GAME_WIDTH//2, 50)
    draw_text("player 2: " + str(player2score), 40, WHITE, GAME_WIDTH//2, 80)

    handle_collision(ball, player1, player2)

    if (ball.x < 0):
        player2score += 1
        ball.reset()
    if (ball.x > 1250):
        player1score += 1
        ball.reset()

    if player1score == WINNING_SCORE:
        game_over = True
        over_msg = "Player 1 wins!"
    if player2score == WINNING_SCORE:
        game_over = True
        over_msg = "Player 2 wins!"

    if game_over == True:
        draw_text(over_msg, 60, WHITE, GAME_WIDTH//2, GAME_HEIGHT//2)
        # pygame.display.update()
        # pygame.time.delay(3000)
        # ball.reset()
        # player1score = 0
        # player2score = 0


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


# New