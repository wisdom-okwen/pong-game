import pygame as pg
from pygame.locals import *
import ball, paddle

pg.init()   #initialize pygame

#set all needed colors
DARK_BLUE = (8, 46, 171)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#object variables
paddle_color = WHITE
ball_color = YELLOW
caption = "Pong Game"
image = pg.image.load("logo.jpg")

#window variables
WIDTH, HEIGHT = 700, 500
background_color = DARK_BLUE
FPS = 60    #frames per second

#setting up the window
logo = pg.display.set_icon(image)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(caption) #set title of game

def draw(screen):
    #draw objects on screen
    screen.fill(background_color)
    pg.display.update()
    
    
def main():
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        draw(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #if close button pressed
                run = False
                break
    pg.quit() #quit game
             

