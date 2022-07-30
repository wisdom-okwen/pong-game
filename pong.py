import pygame as pg
from datetime import time
from pygame.locals import *
import ball, paddle, mid_line

pg.init()   #initialize pygame

#set all needed colors
TEAL = (0, 102, 102)
MAROON = (110, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#window variables
WIDTH, HEIGHT = 800, 400
background_color = TEAL
FPS = 70    #frames per second

#object variables
paddle_color, paddle_height, paddle_width = MAROON, 80, 10
ball_color, ball_radius = YELLOW, 7
line_color, line_start, line_end = WHITE, (WIDTH//2, HEIGHT//8), (WIDTH//2, HEIGHT-HEIGHT//8)
caption = "Pong Game"
image = pg.image.load("logo.jpg")

#setting up the window
logo = pg.display.set_icon(image)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(caption) #set title of game

def draw(screen, paddles, ball1, line1):
    #draw objects on screen
    screen.fill(background_color)
    for pad in paddles:
        pad.draw_rect(screen)
    
    ball1.draw_ball(screen)
    line1.draw_line(screen)
    pg.display.update()
    
def handle_paddle_movement(keys, left_paddle, right_paddle):
    #move paddles based on keyboard entries
    if keys[pg.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move_paddle(up=True)
    if keys[pg.K_s] and left_paddle.y + left_paddle.velocity + left_paddle.height <= HEIGHT:
        left_paddle.move_paddle(up=False)
    if keys[pg.K_DOWN] and right_paddle.y + right_paddle.velocity + right_paddle.height <= HEIGHT:
        right_paddle.move_paddle(up=False)
    if keys[pg.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move_paddle(up=True)
        
def ball_collisions(ball, left_paddle, right_paddle):
    #check for collision with top and bottom walls
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1 
       
    #check collision with paddles 
    if  ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1  
    
def main():
    clock = pg.time.Clock() #set pygame clock
    run = True
    left_paddle = paddle.Paddle(0, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height, paddle_color)
    right_paddle = paddle.Paddle(WIDTH-paddle_width, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height, paddle_color)
    ball1 = ball.Ball(WIDTH//2, HEIGHT//2, ball_radius, ball_color)
    line1 = mid_line.Line(line_start, line_end, line_color)
    while run:
        clock.tick(FPS)
        
        draw(screen, [left_paddle, right_paddle], ball1, line1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #if close button pressed
                run = False
                break
        
        keys = pg.key.get_pressed() #get all keyboard inputs
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball1.move_ball()
        ball_collisions(ball1, left_paddle, right_paddle)
    pg.quit() #quit game
             

