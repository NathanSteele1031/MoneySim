import pygame, items

class PersonPanel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def display_person_info(self, screen, person):
        """
        Call draw before calling this method so it looks right
        """
        if person is None:
            return
        font = pygame.font.Font(None, 20)
        text = font.render(f"X: {person.x}, Y: {person.y}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 10))
        text = font.render(f"Money: {person.money} Needs: {person.needs}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 25))
        
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

class ItemPanel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def display_item_info(self, screen, item: items.Item):
        if item is None:
            return
        font = pygame.font.Font(None, 20)
        text = font.render(f"Name: {item.name}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 35))
        text = font.render(f"Description: {item.description}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 45))
        text = font.render(f"Demand: {item.demand}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 55))
        text = font.render(f"X: {item.x}, Y: {item.y}", True, (255, 255, 255))
        screen.blit(text, (self.x + 10, self.y + 65))