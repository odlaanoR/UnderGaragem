import pygame
from pygame.locals import *
from sys import exit


pygame.init()
largura = 640
altura = 480
velocidade = 7
y = 1
x = 1
cor_acoes = ((150,75,0))
cor_luta = ((150,75,0))
cor_agir = ((150,75,0))
cor_item = ((150,75,0))
cor_mercy = ((150,75,0))

fonte = pygame.font.SysFont('arial', 30, True, False) 
janela = pygame.display.set_mode((largura, altura))
gameover = False
pygame.display.set_caption('Poggers')
icon = pygame.image.load('images.png')
pygame.display.set_icon(icon)
musicaFundo = pygame.mixer.music.load('megalovania.mp3')
pygame.mixer.music.play(-1)
gameoverjanela = pygame.display.set_mode((largura, altura))

fps = pygame.time.Clock()
cor = ((255,0,0))
vida = 92
vidaAtual = 92

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo
    vidaAtual = 92
    x = 1
    y = 1
    gameover = False
    musicaFundo = pygame.mixer.music.load('megalovania.mp3')
    pygame.mixer.music.play(-1)
    
while True:
    fps.tick((60))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
            
    janela.fill((0,0,0))
    textoVida = f'HP: {vidaAtual}/{vida}'
    texto_formatado = fonte.render(textoVida,True, (255, 255, 255)) 
    circulo = pygame.draw.circle(janela, (cor), (x, y), 10)
    caixa = pygame.draw.rect(janela, (255,255,255),(10, 190, 620, 180), width=7)
    lutar = pygame.draw.rect(janela, cor_luta, (50, 440, 100, 30), width=2)
    agir = pygame.draw.rect(janela,cor_agir, (190, 440, 100, 30), width=2)
    item = pygame.draw.rect(janela,cor_item, (330, 440, 100, 30), width=2)
    mercy = pygame.draw.rect(janela,cor_mercy, (470, 440, 100, 30), width=2)
    janela.blit(texto_formatado,(260, 385))
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_x]:
        velocidade = 4.5
    else:
        velocidade = 7
    
    if teclas[pygame.K_z]:
        cor = (0,0,255)
    else:
        cor = (255,0,0)
     
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
        
    if circulo.colliderect(caixa):
        vidaAtual -= 1
    
    if circulo.colliderect(lutar):
        cor_luta = (255,255,0)
    else:
        cor_luta = cor_acoes
    
    if circulo.colliderect(agir):
        cor_agir = (255,255,0)
    else:
        cor_agir = cor_acoes
    
    if circulo.colliderect(item):
        cor_item = (255,255,0)
    else:
        cor_item = cor_acoes
    
    if circulo.colliderect(mercy):
        cor_mercy = (255,255,0)
    else:
        cor_mercy = cor_acoes
    
    if vidaAtual <= 0:
        gameover = True
        tocouGameOver = False
        while gameover:
            if not tocouGameOver:
                pygame.mixer.music.fadeout(280)
                gameoverMusica = pygame.mixer.music.load('gameovertheme.mp3')
                pygame.mixer.music.play(-1)
                tocouGameOver = True
                
            pygame.display.update()
            gameoverjanela.fill((0,0,0))
            gameoverImg = pygame.image.load('gameover.png')
            gameoverjanela.blit(gameoverImg, (130,15))
            textoGameOver = 'Pressione R para reiniciar'
            ggTextoformatado = fonte.render(textoGameOver, True,(255,255,255))
            gameoverjanela.blit(ggTextoformatado, (50, 400))
            
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        reiniciar_jogo()

        
    
    pygame.display.flip()
    