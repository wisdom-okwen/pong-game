import pygame as pg
from pygame.locals import *
import ball, paddle

pg.init() #initialize game

#set all needed colors
DARK_BLUE = (8, 46, 171)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#other variables
background_color = DARK_BLUE
paddle_color = WHITE
caption = "Pong Game"

#setting up the window
WIDTH, HEIGHT = 960, 800
screen = pg.display.set_mode(WIDTH, HEIGHT)


pg.display.set_caption(caption) #set title of game


def main():
    running = True
    while running:
        for event in pg.event.get():
            if event == pg.QUIT:
                running = False
    pg.display.update()           
    return 

pg.quit() #quit game