import pygame
import time
import random
import sys
from data import soundEffect as se # type: ignore


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255, 255, 102)

disWidth = 800
disHeight = 600
dis = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption("Snake Computer Game by Далтон М. Хэмман")

clock = pygame.time.Clock()

snakeSpeed = 20
frameRate = 60
snakeBlock = 10

fontStyle = pygame.font.SysFont("timesnewroman", 25)
scoreFont = pygame.font.SysFont("centurygothic", 25)

def yourScore(score):
    value = scoreFont.render ("Your Score : " + str(score), True, yellow)
    dis.blit(value, [0,0])
    
def snake(snakeBlock, snakeList):
    for x in snakeList: pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])

def message(msg,color):
    msg = fontStyle.render(msg, True, color)
    dis.blit(msg, [disWidth/6, disHeight/3])

def gameLoop():
    gameOver = False
    gameClose = False
    
    x1 = disWidth / 2
    y1 = disHeight / 2
    
    x1Change = 0
    y1Change = 0
    
    snakeList = []
    length_of_snake = 1
    
    foodX = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
    foodY = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
    se.mainSong.set_volume(0.2)
    se.mainSong.play(-1)
    while not gameOver:
        while gameClose == True:
            se.mainSong.fadeout(2)
            dis.fill(blue)
            message("You Lost! Press Q to Quit or C to Play Again!", red)
            yourScore(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1Change = 0
                    y1Change = -snakeBlock
                elif event.key == pygame.K_DOWN or event.key ==  pygame.K_s:
                    x1Change = 0
                    y1Change = snakeBlock

                    
        
        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True
        x1 += x1Change
        y1 += y1Change
        dis.fill(blue)
        
        pygame.draw.rect(dis, green, [foodX, foodY, snakeBlock, snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        if len(snakeList) > length_of_snake:
            del snakeList [0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
                
        snake(snakeBlock, snakeList)
        yourScore(length_of_snake - 1)
        
        pygame.display.update()

        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
            foodY = round (random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
            length_of_snake += 1
            se.nom.play()
            
        clock.tick(frameRate)
        time.sleep(1.0 / snakeSpeed)
    pygame.quit()
    
    
gameLoop()