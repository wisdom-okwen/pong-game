import pygame as pg
from pygame.locals import *
import ball, paddle

pg.init()   #initialize pygame

#set all needed colors
TEAL = (0, 102, 102)
MAROON = (110, 0, 0)
YELLOW = (255, 255, 0)

#object variables
paddle_color, paddle_height, paddle_width = MAROON, 100, 20
ball_color, ball_radius = YELLOW, 10
caption = "Pong Game"
image = pg.image.load("logo.jpg")

#window variables
WIDTH, HEIGHT = 800, 400
background_color = TEAL
FPS = 60    #frames per second

#setting up the window
logo = pg.display.set_icon(image)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(caption) #set title of game

def draw(screen, paddles, ball1):
    #draw objects on screen
    screen.fill(background_color)
    for pad in paddles:
        pad.draw_rect(screen)
    
    ball1.draw_ball(screen)
    pg.display.update()
    
    
def main():
    clock = pg.time.Clock()
    run = True
    left_paddle = paddle.Paddle(0, 0, paddle_width, paddle_height, paddle_color)
    right_paddle = paddle.Paddle(WIDTH-paddle_width, 0, paddle_width, paddle_height, paddle_color)
    ball1 = ball.Ball(WIDTH//2, HEIGHT//2, ball_radius, ball_color)
    while run:
        clock.tick(FPS)
        
        draw(screen, [left_paddle, right_paddle], ball1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #if close button pressed
                run = False
                break
    pg.quit() #quit game
             

