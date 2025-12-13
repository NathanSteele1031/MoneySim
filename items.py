import pygame

class Item:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.demand = 0
        self.need_satisfied = []
        self.x = 0
        self.y = 0
    
    def add_demand(self, amount):
        self.demand += amount
    
    def remove_demand(self, amount):
        self.demand -= amount
    
    def set_cord(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 5)

class Weapon(Item):
    def __init__(self):
        super().__init__()
        self.description += "Weapon "
    
class Jewelry(Item):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("shiney")
        self.description += "Jewelry "

class Braslet(Jewelry):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("round")
        self.description += "Braslet "

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("sharp")
        self.description += "Sword "

class Club(Weapon):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("blunt")
        self.description += "Club "