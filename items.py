import pygame, json

def load_json_items(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

class Item:
    def __init__(self, name, description="", demand=0, need_satisfied=[], x=0, y=0):
        self.name = name
        self.description = description
        self.demand = demand
        self.need_satisfied = need_satisfied
        self.x = x
        self.y = y
    
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
    def __init__(self, name, description="", demand=0, need_satisfied=[], x=0, y=0):
        super().__init__(name, description, demand, need_satisfied, x, y)
    
class Jewelry(Item):
    def __init__(self, name, description="", demand=0, need_satisfied=[], x=0, y=0):
        super().__init__(name, description, demand, need_satisfied, x, y)

class Consumable(Item):
    def __init__(self, name, description="", demand=0, need_satisfied=[], x=0, y=0):
        super().__init__(name, description, demand, need_satisfied, x, y)