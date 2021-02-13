import pygame

pygame.init()

display_width = 800
display_height = 600
random = (1,800)
x=400
y=500
x_change=0
y_change=0
y2=600
x2 = (1,800)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mario 64')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('mario.png')
carImg2 = pygame.image.load('grib.png')
Ball_Img = pygame.image.load('block.png')
gameover_Img = pygame.image.load('гейм овер.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def car2(x,y):
    gameDisplay.blit(carImg2, (x,y))

def Ball(x,y):
    gameDisplay.blit(Ball_Img, (x,y))

while not crashed:
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
        ######################
       
        
    
    x += x_change
    y += y_change

    y2-=5
    y_ball-=5
    ##         
    gameDisplay.fill(white)
    
    ##
    if abs(x+193-x_ball-32)<=193+32 and abs(y+65-y_ball-32)<=65+32:
         gameDisplay.blit(gameover_Img, (400,300))



    if abs(x+193-x_car2-32)<=193+32 and abs(y+65-y_car2-32)<=65+32:
        gameDisplay.blit(gameover_Img, (400,300))

    if y_ball < 0:
        y_ball = 600
        x_ball = random.randint(1,800)

    if y_car2 < 0:
        y2_car2 = 600
        x2_car2 = random.randint(1,800)

    car(x,y)
    car2(x2, y2)
    Ball(x_ball,y_ball)
    

pygame.quit()
quit()