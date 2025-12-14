import pygame, random, json, curses
import inventory

class Person():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.money = 0
        self.inventory = inventory.Inventory()
        self.needs = self.random_needs()
    
    def random_needs(self):
        with open("GameData/needs.json", "r") as f:
            needs = json.load(f)
        return random.choice(needs["item_properities"])
    
    def random_move(self, terminal_view=False):
        if terminal_view:
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)
        else:
            self.x += random.randint(-1, 1) * 10
            self.y += random.randint(-1, 1) * 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)
    
    def draw_terminal(self, screen):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        screen.addch(self.y, self.x, "P", curses.color_pair(1))