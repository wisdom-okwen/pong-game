import pygame as pg

class Ball:
    def __init__(self, x, y, radius, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
       
    def draw_ball(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
        
    def move_ball(self):
        pass