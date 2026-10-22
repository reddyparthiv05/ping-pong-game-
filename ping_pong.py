import pygame #imports the pygame library
import random #imports the random library 
import sys #imports sys 

pygame.init() #start the pygame

WIDTH,HEIGHT = 800,500 #set the width and height of the game window
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #creates the gaming window
pygame.display.set_caption("Ping Pong Game") #assigns the window a title

WHITE = (255,255,255) 
BLACK = (0,0,0)

PADDLE_WIDTH = 10 #sets the paddles width as 10
PADDLE_HEIGHT = 100 #sets the padlles height as 100
paddle_speed = 6 #sets the paddle speed as 6

p1 = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2 ,PADDLE_WIDTH, PADDLE_HEIGHT) #creates the player 1 paddle

p2 = pygame.Rect(WIDTH-40, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #creates the player 2 paddle

ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10,20 ,20) #cretes a ball at the middle of the screen
ball_speed_x = 5*random.choice((-1,1)) #sets the ball speed in the horizontal direction
ball_speed_y = 5*random.choice((-1,1)) #sets the ball speed in the vertical direction
 
score1 = 0 #intializes the score of player 1 as 0 
score2 = 0 #intializes the score of player 2 as 0
font = pygame.font.SysFont(None,50)  #sets the font of the game window as 5

clock = pygame.time.Clock() #creates a clock for the game 
FPS= 60

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE,p1) # draw the paddle of player1
    pygame.draw.rect(screen,WHITE,p2) # draw the paddle of player2
    pygame.draw.ellipse(screen,WHITE,ball) # draw the paddle of the white ball
    pygame.draw.aaline(screen,WHITE,(WIDTH//2, 0), (WIDTH//2, HEIGHT)) #draws a line in the centre 

    score_text1 = font.render(str(score1), True, WHITE) #convert the score of player 1 into a string
    score_text2 = font.render(str(score2), True, WHITE) #convert the score of player 2 into a string
    screen.blit(score_text1, (WIDTH//4, 20)) #displays the score of the first player
    screen.blit(score_text2, (WIDTH*3//4, 20)) #displays the score of the second player

    pygame.display.flip() #updates the screen 
    
def reset_ball(): 
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2) #moves the ball to the centre of the game window
    ball_speed_x *= random.choice((-1,1)) #changes into horizontal direction
    ball_speed_y *= random.choice((-1,1)) #changes into verical direction

running = True 
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks wheather the QUIT button is clicked 
            pygame.quit() #closes the pygame
            sys.exit() #exists the programme

    keys = pygame.key.get_pressed() #detects the keys which are pressed correctly
    if keys[pygame.K_w] and p1.top > 0: #moves the left side paddle up when w is pressed
        p1.y -= paddle_speed #decreases the y coordinates to move down 
    if keys[pygame.K_s] and p1.bottom <HEIGHT: #moves the left side paddle down when s is clicked
        p1.y +=paddle_speed #increases the x coordinates to move up

    if keys[pygame.K_UP] and p2.top>0: #moves the right side paddle up when the up button is pressed
        p2.y -= paddle_speed #decreases the y coordinates so that the paddle moves down
    if keys[pygame.K_DOWN] and p2.bottom < HEIGHT: #moves the right side paddle down when the down button is pressed
        p2.y +=paddle_speed #increases the y coordinates so that the paddle moves up

    ball.x += ball_speed_x #move sthe ball horizontally
    ball.y += ball_speed_y #move the ball vertically
 
    if ball.top <=0 or ball.bottom>= HEIGHT: #checks if the ball touches the top or bottom of the screen 
        ball_speed_y *= -1 #reverses the vertical direction 

    if ball.colliderect(p1) or ball.colliderect(p2): #checks wheather the ball touches either paddle 
        ball_speed_x *= -1 #reverses the ball to horizontal direction 

    if ball.left<=0: #check if the ball crosse sthe left boundary
        score2+=1 #increase the score of player 2 by 1 point
        reset_ball() #reset the ball to the center 

    if ball.right>=WIDTH: #checks if the ball crosses the right boundary
        score1+=1 #increases the score of player 1 by 1 point 
        reset_ball() #resets the ball to the center

    draw_objects() 

            