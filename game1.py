import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))


class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 13
        self.dx = 5  # right
        self.dy = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (10, 200, 150), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

appleImage = pygame.image.load('c:/Users/Шкимишки/Documents/Work2/pygame/snake/fruit.png')
apple_x = random.randint(0, 770)
apple_y = random.randint(0, 570)
def apple(x, y):
    screen.blit(appleImage, (x, y))

def isCollided(x1, y1, x2, y2):
    #distance
    d = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if d < 19:
        return True
    else:
        return False

snake = Snake()

running = True

d = 5
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 25)
score_x = 10 
score_y = 10

def Score(x, y):
    score = font.render("SCORE: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

FPS = 30

clock = pygame.time.Clock()

k1_pressed = False

while running:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = d

    snake.move()
    screen.fill((0, 0, 0))
    snake.draw()
    apple(apple_x, apple_y)
    Score(score_x, score_y)

    #collision between snake and apple
    coll = isCollided(snake.elements[0][0], snake.elements[0][1], apple_x, apple_y)

    if coll:
        score_value += 1
        apple_x = random.randint(0, 770)
        apple_y = random.randint(0, 570)
        snake.is_add = True

    #gameover 
    if snake.elements[0][0]>800 or snake.elements[0][0]<0 or snake.elements[0][1]<0 or snake.elements[0][1]>600:
        gameover = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameover, (320, 270))
        snake.dx = 0
        snake.dy = 0


    pygame.display.flip()