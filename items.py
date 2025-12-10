class Item:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.demand = 0
        self.need_satisfied = []
    
    def add_demand(self, amount):
        self.demand += amount
    
    def remove_demand(self, amount):
        self.demand -= amount

class Weapon(Item):
    def __init__(self):
        super().__init__()
    
class Jewelry(Item):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("shiney")

class Braslet(Jewelry):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("round")

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("sharp")

class Club(Weapon):
    def __init__(self):
        super().__init__()
        self.need_satisfied.append("blunt")