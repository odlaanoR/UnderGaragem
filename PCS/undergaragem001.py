import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura = 480
velocidade = 7
x = 65
y = 450
cor_acoes = ((150,75,0))
cor_luta = ((150,75,0))
cor_agir = ((150,75,0))
cor_item = ((150,75,0))
cor_mercy = ((150,75,0))
fps = pygame.time.Clock()
vida = 92
vidaAtual = 92

fonte = pygame.font.SysFont('arial', 30, True, False)
pygame.display.set_caption('Poggers')
icon = pygame.image.load('images.png')
pygame.display.set_icon(icon)
musicaFundo = pygame.mixer.music.load('megalovania.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

janela = pygame.display.set_mode((largura, altura))
gameover = False
gameoverjanela = pygame.display.set_mode((largura, altura))

class Alma(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/alma.png'))
        self.sprites.append(pygame.image.load('assets/almaazul.png'))
        self.sprites.append(pygame.image.load('assets/almaverde.png'))       
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = x, y

    def update(self):
        self.rect.center = x, y
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        
alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo
    vidaAtual = 92
    x = 65
    y = 445
    gameover = False
    musicaFundo = pygame.mixer.music.load('megalovania.mp3')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

while True:
    fps.tick((60))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT and not circulo.colliderect(mercy):
                x += 140
            if evento.key == K_LEFT and not circulo.colliderect(lutar):
                x -= 140
            if evento.key == K_z and circulo.colliderect(lutar):
                print('me clicaram')
                
            if evento.key == K_z and circulo.colliderect(agir):
                print('me clicaram2')
            if evento.key == K_z and circulo.colliderect(item):
                print('me clicaram3')
            if evento.key == K_z and circulo.colliderect(mercy):
                print('me clicaram4')
                
        if evento.type == KEYDOWN:
            #print("Apertou algo!")
            if evento.key == K_F11:
                #print("Pondo em tela cheia...")
                pygame.display.toggle_fullscreen()
            elif evento.key == K_j:
                print('mudando o estado da alma para ', {alma.estado})
                alma.estado += 1
                if alma.estado == 3:
                    alma.estado = 0
        if evento.type == QUIT:
            pygame.quit()
            exit()
            
    janela.fill((0,0,0))
    textoVida = f'HP: {vidaAtual}/{vida}'
    
    texto_formatado = fonte.render(textoVida,True, (255, 255, 255)) 
    caixa = pygame.draw.rect(janela, (255,255,255),(10, 190, 620, 180), width=7)
    circulo = pygame.draw.circle(janela, (0,255,0), (x+0.2, y+0.8), 7.6)
    lutar = pygame.draw.rect(janela, cor_luta, (50, 430, 100, 40), width=2)
    agir = pygame.draw.rect(janela,cor_agir, (190, 430, 100, 40), width=2)
    item = pygame.draw.rect(janela,cor_item, (330, 430, 100, 40), width=2)
    mercy = pygame.draw.rect(janela,cor_mercy, (470, 430, 100, 40), width=2)
    janela.blit(texto_formatado,(260, 385))
    teclas = pygame.key.get_pressed()
    
    if alma.estado == 1:
        y += 0
        pygame.display.set_caption("Você está azul agora!")
            
    elif alma.estado == 2 :
        velocidade = 0
        pygame.display.set_caption("Você está verde!")
    else:
        pygame.display.set_caption("Você se enche de DETERMINAÇÃO")
        velocidade = 0

    artes.draw(janela)
    artes.update()

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
                pygame.mixer.music.set_volume(0.6)
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
    