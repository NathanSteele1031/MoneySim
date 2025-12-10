import pygame

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