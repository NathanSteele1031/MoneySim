import pygame, random, json

class Person():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.money = 0
        self.assets = []
        self.needs = self.random_needs()
    
    def random_needs(self):
        with open("GameData/needs.json", "r") as f:
            needs = json.load(f)
        return random.choice(needs["item_properities"])
    
    def random_move(self):
        self.x += random.randint(-1, 1) * 10
        self.y += random.randint(-1, 1) * 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)