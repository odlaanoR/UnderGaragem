import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()
largura = 640
altura = 480
velocidade = 7
x = 65
y = 450

fps = pygame.time.Clock()
vida = 92
vidaAtual = 92

corAcoes = ((150,75,0))
corLuta = corAcoes
corAgir = corAcoes
corItem = corAcoes
corMercy = corAcoes

mostrarMsgLutar = False
mostrarMsgAgir = False
mostrarMsgItem = False
mostrarMsgMercy = False


fonte = pygame.font.SysFont('arial', 30, True, False)
fonteBatalha = pygame.font.SysFont('comicsans', 20, True, False)
pygame.display.set_caption('Poggers')
icon = pygame.image.load('assets/images.png')
pygame.display.set_icon(icon)
musicaFundo = pygame.mixer.music.load('assets/megalovania.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

class Janelas():
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura,altura))
        self.telaAtual = 'ações'
        
    def mudarTela(self,novaTela):
        self.telaAtual = novaTela
    
    def atualizaTela(self):
        pygame.display.flip()
        
    def escreveTexto(self, texto, fonte, cor, posicao):
        txt = fonte.render(texto,True,cor)
        self.tela.blit(txt,posicao)
        
    def textoDelay(self, texto,fonte, cor, posicao, delay):
        txtAtual =''
        for letra in texto:
            txtAtual += letra
            txtRenderizado = fonte.render(txtAtual,True,cor)
            self.tela.blit(txtRenderizado,posicao)
            time.sleep(delay)
    
    def corFundo(self,cor=(0,0,0)):
        self.tela.fill(cor)



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
        
janela = Janelas(largura,altura)
alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo
    vidaAtual = 92
    x = 65
    y = 445
    gameover = False
    musicaFundo = pygame.mixer.music.load('assets/megalovania.mp3')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
    janela.mudarTela('ações')
    
while True:
    fps.tick((60))
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT and not alma.rect.colliderect(mercy):
                x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(lutar):
                x -= 140
            if evento.key == K_z and alma.rect.colliderect(lutar):
                mostrarMsgLutar = True
            if evento.key == K_z and alma.rect.colliderect(agir):
                mostrarMsgAgir = True
            if evento.key == K_z and alma.rect.colliderect(item):
                mostrarMsgItem = True
            if evento.key == K_z and alma.rect.colliderect(mercy):
                mostrarMsgMercy = True
  
            if evento.key == K_x:
                mostrarMsgLutar = False
                mostrarMsgAgir = False
                mostrarMsgItem = False
                mostrarMsgMercy = False
                x = 65
                y = 450
                janela.mudarTela('ações')
                janela.atualizaTela()
                
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
            
    janela.corFundo()
    caixa = pygame.draw.rect(janela.tela, (255,255,255),(10, 190, 620, 180), width=7)
    lutar = pygame.draw.rect(janela.tela, corLuta, (50, 430, 100, 40), width=2)
    agir = pygame.draw.rect(janela.tela,corAgir, (190, 430, 100, 40), width=2)
    item = pygame.draw.rect(janela.tela,corItem, (330, 430, 100, 40), width=2)
    mercy = pygame.draw.rect(janela.tela,corMercy, (470, 430, 100, 40), width=2)
    janela.escreveTexto(f'HP:{vidaAtual}/{vida}', fonte, (255,255,255),(260,385))
    
    #teclas = pygame.key.get_pressed() 
    #if teclas[pygame.K_w]:
        #y -= 7

    if alma.estado == 1:
        y += 0
        pygame.display.set_caption("Você está azul agora!")
            
    elif alma.estado == 2 :
        velocidade = 0
        pygame.display.set_caption("Você está verde!")
    else:
        pygame.display.set_caption("Você se enche de DETERMINAÇÃO")
        velocidade = 0

    artes.draw(janela.tela)
    artes.update()

    if alma.rect.colliderect(caixa):
        vidaAtual -= 0
    
    if alma.rect.colliderect(lutar):
        corLuta = (255,255,0)
    else:
        corLuta = corAcoes
    
    if alma.rect.colliderect(agir):
        corAgir = (255,255,0)
    else:
        corAgir = corAcoes
    
    if alma.rect.colliderect(item):
        corItem = (255,255,0)
    else:
        corItem = corAcoes
    
    if alma.rect.colliderect(mercy):
        corMercy = (255,255,0)
    else:
        corMercy = corAcoes
    
    if mostrarMsgLutar:
        janela.escreveTexto('Wilson Tremba',fonteBatalha,(255,255,255),(43,205))
        x = 30
        y = 220
        
    if mostrarMsgAgir:
        janela.escreveTexto('Checar',fonteBatalha,(255,255,255),(43,205))
        x = 30
        y = 220
    if mostrarMsgItem:
        janela.escreveTexto('Cuscuz Paulista',fonteBatalha,(255,255,255),(43,205))
        x = 30
        y = 220
    if mostrarMsgMercy:
        janela.escreveTexto('Piedade',fonteBatalha,(255,255,255),(43,205))
        x = 30
        y = 220
         
    
    if vidaAtual <= 0:
        janela.mudarTela('gameover')
        tocouGameOver = False
        while janela.telaAtual == 'gameover':
            if not tocouGameOver:
                pygame.mixer.music.fadeout(280)
                gameoverMusica = pygame.mixer.music.load('assets/gameovertheme.mp3')
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play(-1)
                tocouGameOver = True
                janela.atualizaTela()
            
            janela.corFundo()
            gameoverImg = pygame.image.load('assets/gameover.png')
            janela.tela.blit(gameoverImg, (130,15))
            janela.escreveTexto('Pressione R para reiniciar', fonte, (255,255,255), (50, 400))
            janela.atualizaTela()
                   
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        reiniciar_jogo()
                        
    janela.atualizaTela()
    
