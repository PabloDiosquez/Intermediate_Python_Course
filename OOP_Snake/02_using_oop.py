# Make it all object oriented by converting the code in various classes

import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Snake:
    def __init__(self, parent_screen, lenght):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("OOP_Snake/resources/block.jpg").convert()
        self.direction = "down"

        self.lenght = lenght
        self.x = [SIZE] * lenght
        self.y = [SIZE] * lenght

    def draw(self):
        self.parent_screen.fill((33, 150, 64))

        for i in range(self.lenght):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):

        for i in range(self.lenght-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE

        self.draw()

    def move_up(self):
        self.direction = "up"
    
    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def increase_length(self):
        self.lenght += 1
        self.x.append(-1)
        self.y.append(-1)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("OOP_Snake/resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
    
    def move(self):
        self.x = random.randint(0,14) * SIZE
        self.y = random.randint(0,14) * SIZE

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600, 600))
        self.surface.fill((33, 150, 64))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.lenght-1}", True, (255,255,255))
        self.surface.blit(score, (400,10))
            
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            

            self.play()
            time.sleep(0.2)
                

if __name__ == "__main__":
    game = Game()
    game.run()