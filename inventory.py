class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def pop_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        print(f"Error: No item at index {index}")
        return None