import pygame
import random
import time
pygame.init()

display_width = 1000
display_height = 700

x=500
y=100
x_change=0
y_change=0
y2=600
x2 = random.randint(1,1000)
x_ball = random.randint(1,1000)
y_ball=600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mario 64')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('сантехник2.png')
carImg2 = pygame.image.load('гриб2.png')
Ball_Img = pygame.image.load('кирпич2.png')
gameover_Img = pygame.image.load('гейм овер2.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def car2(x,y):
    gameDisplay.blit(carImg2, (x,y))

def Ball(x,y):
    gameDisplay.blit(Ball_Img, (x,y))

while not crashed:
    pygame.display.update()

    for event in pygame.event.get():
        clock.tick(100)
        if event.type == pygame.QUIT:
            crashed = True

        ############################

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -7
            elif event.key == pygame.K_RIGHT:
                x_change = 7
            elif event.key == pygame.K_UP:
                y_change = -7
            elif event.key == pygame.K_DOWN:
                y_change = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
        ######################
       
     
    
    x += x_change
    y += y_change

    y2-=4
    y_ball-=4
    ##         
    gameDisplay.fill(white)
    
    ##
    # if abs(x+121)<x_ball+0 or abs(x+0)<x_ball+170:
    #     if abs(y+158)>y_ball+0 or abs(y+0)<y_ball+166:
    #         print(x, x_ball)
    #         gameDisplay.blit(gameover_Img, (0,0))

   

    # if abs(x+121)>x2+0 or abs(x+0)<x2+150:
    #     if abs(y+158)>y2+0 or abs(y+0)<y2+150:

    #         gameDisplay.blit(gameover_Img, (0,0))



    if y_ball < 0:
        y_ball = 600
        x_ball = random.randint(1,800)

    if y2 < 0:
        y2 = 600
        x2 = random.randint(1,800)

    
    car2(x2, y2)
    Ball(x_ball,y_ball)

    print(gameDisplay.get_at((int(x+60.5),int(y+79))))
    color=gameDisplay.get_at((int(x+75),int(y+75)))
    car(x,y)
    if color!=white:
        gameDisplay.blit(gameover_Img, (0,0))
        time.sleep(0.5)


    
pygame.quit()
quit()