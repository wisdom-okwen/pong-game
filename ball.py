import pygame as pg

class Ball:
    MAX_VEL = 5
    border = 15
    def __init__(self, x, y, radius, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.color = color
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
       
    def draw_ball(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.border)
        
        
    def move_ball(self):
        self.x += self.x_vel 
        self.y += self.y_vel
        
    def reset_ball(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1