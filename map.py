import pygame, curses

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

class TerminalMap:
    def __init__(self, charwidht, charheight):
        self.charwidth = charwidht
        self.charheight = charheight
        self.objects = []
    
    def draw(self, screen: curses.window):
        for x in range(0, self.charwidth):
            for y in range(0, self.charheight):
                screen.addch(y, x, "_")
        for item in self.objects:
            item.draw_terminal(screen)
    
    def add_object(self, object_value):
        self.objects.append(object_value)
    
    def pop_object(self, object_index):
        self.objects.pop(object_index)