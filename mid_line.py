import pygame as pg

class Line:
    def __init__(self, start, end, color):
        self.start = start
        self.end = end
        self.color = color
        
    def draw_line(self, screen):
        pg.draw.line(screen, self.color, self.start, self.end)