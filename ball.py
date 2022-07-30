import pygame as pg

class Ball:
    MAX_VEL = 2
    border = 15
    def __init__(self, x, y, radius, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
       
    def draw_ball(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.border)
        
        
    def move_ball(self):
        self.x += self.x_vel 
        self.y += self.y_vel