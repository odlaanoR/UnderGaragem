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
        
    def corFundo(self,cor=(0,0,0)):
        self.tela.fill(cor)

class Acoes():
    corPadrao = (150,75,0)
    novaCor = (255,255,0)
    
    def __init__(self, pos_x, msg):
        self.botao = pygame.Rect(pos_x, 430, 100, 40)
        self.cor = self.corPadrao
        self.mostraMsg = False
        self.mensagem = msg
        
    def desenhaAtos(self):
        pygame.draw.rect(janela.tela, self.cor, self.botao, width=2)

    def checaAlma(self, player):
        if player.colliderect(self.botao):
            self.cor = self.novaCor
        else:
            self.cor = self.corPadrao
            
    def clique(self,player, tecla):
        if tecla == K_z and player.colliderect(self.botao):
            self.mostraMsg = True
            
    def cancelaAto(self):
        self.mostraMsg = False
            
    def atoMensagem(self, fonte):
        if self.mostraMsg:
            janela.tela.blit(fonte.render(self.mensagem, True, (255,255,255)), (43,205))
            
class Ataque():
    def __init__(self, cor , ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y, vel):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.vel = vel
        self.cor = cor
        self.mostrar = True

    def atualizar(self, alma_rect):
        if self.mostrar == True:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= 640:
                self.retangulo.x = 0
            if self.retangulo.colliderect(alma_rect):
                print("colidiu!")
                self.mostrar = False
                return True
            return False
            
    def draw(self):
        if self.mostrar == True:
            self.sla1 = pygame.draw.rect(janela.tela, self.cor, self.retangulo)
 
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
botoes = [
    Acoes(50, "Wilson Tremba"),
    Acoes(190, "Checar"),
    Acoes(330, "Cuscuz Paulista"),
    Acoes(470, "Piedade"),
    ]

alma = Alma()
ataque = Ataque((255,255,255), 0, 110, 20, 20, 3, 0, 5)
artes = pygame.sprite.Group()
artes.add(alma)

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo, bateu
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
            
            if evento.key == K_RIGHT and not alma.rect.colliderect(botoes[3].botao) and not any(botao.mostraMsg for botao in botoes):
                x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(botoes[0].botao) and not any(botao.mostraMsg for botao in botoes):
                x -= 140
                            
            if evento.key == K_z:
                for botao in botoes:
                    botao.clique(alma.rect, evento.key)
                x = 30
                y = 220
       
            if evento.key == K_x:
                for botao in botoes:
                    botao.cancelaAto()
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
    janela.escreveTexto(f'HP:{vidaAtual}/{vida}', fonte, (255,255,255),(260,385))
        
    for botao in botoes:
        botao.checaAlma(alma.rect)
        botao.desenhaAtos()
        botao.atoMensagem(fonteBatalha)
        
    if ataque.mostrar:
        ataque.draw()      
        if ataque.atualizar(alma.rect) and ataque.mostrar == False:
            vidaAtual -= 1
        
   #desconsidere isso no jogo normal, é apenas pra testar o ataque lá 
    teclas = pygame.key.get_pressed() 
    if teclas[pygame.K_w]:
        y -= 7
        
    if teclas[pygame.K_s]:
        y += 7
        
    if teclas[pygame.K_d]:
        x += 7
        
    if teclas[pygame.K_a]:
        x -= 7
        
    #Esse aqui botei nos comentários pq fico testando a tela de gameover.
    #if alma.rect.colliderect(caixa):
        #vidaAtual -= 10

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
    
