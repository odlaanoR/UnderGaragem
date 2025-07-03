import pygame
from pygame.locals import *


i = 0

pygame.init()
#Iniciando ^ e setando as dimensões da tela do jogo
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)

cores = [(255,0,0), (0,255,0), (0,0,255)]

#definindo as informações da Janela
icone = pygame.image.load('PCS/assets/alma.png')
pygame.display.set_caption('UnderGaragem')
pygame.display.set_icon(icone)

#iniciando o loop principal do jogo
while True:


    tela.fill("black")

    pygame.draw.circle(tela, cores[i], player_pos, 25)
    if i == 2:
        player_pos.y += 100 * dt
        
    if i == 1 :
        speed = 0
    else:
        speed = 300

    keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
        speed = 0

    if keys[pygame.K_UP]:
        player_pos.y -= speed * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += speed * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += speed * dt




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN :
            if event.key == K_j : 
                i += 1
                print("j")
                if i == 3:
                    i = 0


    pygame.display.flip()
    dt = clock.tick(60) / 1000
