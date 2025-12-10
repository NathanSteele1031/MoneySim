import pygame, random

class Person():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.money = 0
        self.assets = []
    
    def random_move(self):
        self.x += random.randint(-1, 1) * 10
        self.y += random.randint(-1, 1) * 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)