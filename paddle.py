import pygame as pg

class Paddle:
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    def draw_rect(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        
    def move_paddle(self):
        pass
    