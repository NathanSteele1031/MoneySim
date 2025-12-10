import pygame

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
    
    def show_lines(self, screen: pygame.Surface):
        for x in range(0, self.width, 10):
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, self.height))
        for y in range(0, self.height, 10):
            pygame.draw.line(screen, (0, 0, 0), (0, y), (self.width, y))
        
    def move_object(self, object_index, x, y):
        self.objects[object_index].x = x
        self.objects[object_index].y = y