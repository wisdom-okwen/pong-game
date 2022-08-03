import pygame as pg

class Paddle:
    velocity = 4
    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color
        
    def draw_rect(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        
    def move_paddle(self, up=True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity
    
    def reset_pad(self):
        self.x = self.original_x
        self.y = self.original_y
        