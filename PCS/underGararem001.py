import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()
largura = 640
altura = 480
velocidade = 3.2
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
musicaFundo = pygame.mixer.music.load('assets/Project147.mp3')
pygame.mixer.music.set_volume(0.45)
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
        
    def desenhaCaixa(self, caixa):
        self.caixa = pygame.draw.rect(janela.tela, (255,255,255), caixa, width=7)
    
class Acoes(): #to começando a achar que essa classe ta maior doq deveria mas fazer oq
    corPadrao = (150,75,0)
    novaCor = (255,255,0)
    
    def __init__(self, pos_x, msg): 
        self.botao = pygame.Rect(pos_x, 430, 100, 40)
        self.cor = self.corPadrao
        self.mostraMsg = False
        self.mensagem = msg
        self.passou = False
        self.gambiarraMsg = pygame.Rect((0,0,0,0))
        self.mira = pygame.Rect((0,0,0,0))
        self.x_mira = 40
        self.mirando = False
        self.comecaBatalha = False #isso indica se a batalha deve ou não começar
        self.naBatalha = False #e esse aqui impede que o x e o y do jogador seja resetado INFINITAMENTE PQP EU N AGUENTO MAIS (não pensei em um nome melhor)
        self.comecoMira = 0 #tive que criar isso aqui pq a mira tava selecionando automaticamente
        
    def desenhaAcoes(self):
        pygame.draw.rect(janela.tela, self.cor, self.botao, width=2)

    def checaAlma(self):
        if alma.rect.colliderect(self.botao):
            self.cor = self.novaCor
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.wav')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False   
        else:
            self.cor = self.corPadrao
            self.passou = True
            
    def checaClique(self, tecla):
        if tecla == K_z and alma.rect.colliderect(self.botao):
            self.mostraMsg = True  
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.gambiarraMsg = pygame.Rect(30, 215, 10, 10)
            
    def cancelaAcao(self):
        self.mostraMsg = False
            
    def acoesMensagem(self, fonte):
        if self.mostraMsg:
            janela.tela.blit(fonte.render(self.mensagem, True, (255,255,255)), (43,205))

    def confirmaAcao(self, tecla):
        if self.mostraMsg and tecla == K_z and alma.rect.colliderect(self.gambiarraMsg):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.mostraMsg = False
            return True
        return False
    
    def confirmaLuta(self):
        self.mirando = True
        self.comecoMira = pygame.time.get_ticks()
        
    def confirmaAgir(self):
        print('poggers')
        
    def confirmaItem(self):
        print('comeu')
        
    def confirmaPiedade(self):
        print('Mas não estava amarelo')
        
    def mirar(self, tecla):
        if self.mirando:
            pygame.draw.rect(janela.tela, (0, 0, 0), self.gambiarraMsg)
            self.alvo = pygame.image.load('assets/mira.png')
            self.alvo = pygame.transform.scale(self.alvo, (600, 135))
            janela.tela.blit(self.alvo, (20, 205))
            self.x_mira += 5.6
            self.mira = pygame.Rect(self.x_mira, 205, 7, 140)
            pygame.draw.rect(janela.tela, (255,255,255), self.mira)
            tempoAtual = pygame.time.get_ticks()
            if self.x_mira >= 620 or (tecla == K_z and tempoAtual - self.comecoMira >= 100):
                self.mirando = False
                self.x_mira = 40
                self.comecaBatalha = True
            
    def batalhaAcontece(self):
        global x, y, tempoLuta
        if self.comecaBatalha and self.naBatalha == False:
            tempoLuta = pygame.time.get_ticks()
            janela.mudarTela('lutaAcontecendo')
            x = 320
            y = 260
            self.naBatalha = True
        
class Ataque():
    def __init__(self, cor , ataque_x, ataque_y, ataque_w, ataque_h, mov_x, mov_y, vel):
        self.retangulo = pygame.Rect(ataque_x, ataque_y, ataque_w, ataque_h)
        self.mov_x = mov_x
        self.mov_y = mov_y
        self.vel = vel
        self.cor = cor
        self.mostrar = True
        self.contador = 0 #opa coisa nova, não sei se vai ficar aqui por mt tempo, mas nesse ataque padrão vai servir (explico lá embaixo)

    def atualizar(self, alma_rect):
        if self.mostrar == True:
            self.retangulo.x += self.mov_x
            self.retangulo.y += self.mov_y
            if self.retangulo.x >= 530:
                self.retangulo.x = 80
                self.contador += 1
            if self.retangulo.colliderect(alma_rect):
                print("colidiu!")
                self.mostrar = False
                return True
            return False
            
    def draw(self):
        if self.mostrar:
            self.sla1 = pygame.draw.rect(janela.tela, self.cor, self.retangulo)
    
class Alma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/sprites/alma.png'))
        self.sprites.append(pygame.image.load('assets/sprites/almaazul.png'))
        self.sprites.append(pygame.image.load('assets/sprites/almaverde.png'))       
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
ataque = Ataque((255,255,255), 80, 220, 20, 20, 3, 0, 5)
ataque2 = Ataque('white', 90, 250, 40, 40, 10, 0, 5)
ataque3 = Ataque('red', 150, 150, 30, 30, 0, 0, 0)
artes = pygame.sprite.Group()
artes.add(alma)

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo
    vidaAtual = 92
    x = 65
    y = 445
    gameover = False
    musicaFundo = pygame.mixer.music.load('assets/Project147.mp3')
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(-1)
    janela.mudarTela('ações')
    
while True:
    fps.tick((60))
    pygame.display.update()
    eventos = pygame.event.get()
    confirmaAtaque = None
    for evento in eventos:
        if evento.type == KEYDOWN and janela.telaAtual == 'ações':
            confirmaAtaque = evento.key
            if evento.key == K_RIGHT and not alma.rect.colliderect(botoes[3].botao) and not any(botao.mostraMsg for botao in botoes):
                x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(botoes[0].botao) and not any(botao.mostraMsg for botao in botoes):
                x -= 140
        
            if evento.key == K_z:
                for botao in botoes:
                    botao.checaClique(evento.key)
                if botoes[1].confirmaAcao(evento.key):
                    botoes[1].confirmaAgir()
                if botoes[0].confirmaAcao(evento.key):
                    botoes[0].confirmaLuta()
                    botoes[0].batalhaAcontece()
                if botoes[2].confirmaAcao(evento.key):
                    botoes[2].confirmaItem()
                if botoes[3].confirmaAcao(evento.key):
                    botoes[3].confirmaPiedade()
                x = 30
                y = 220

            if evento.key == K_x and not any(botao.mirando for botao in botoes):
                for botao in botoes:
                    botao.cancelaAcao()
                x = 65
                y = 450
            
        if evento.type == QUIT:
            pygame.quit()
            exit()
   
    janela.corFundo()
    janela.escreveTexto(f'HP:{vidaAtual}/{vida}', fonte, (255,255,255),(260,385))
    if janela.telaAtual == 'lutaAcontecendo':
        janela.desenhaCaixa((70, 190, 500, 180))
    else:
        janela.desenhaCaixa((10,180,620,180))
        
    almaDesaparece = any(botao.mirando for botao in botoes) 

    if almaDesaparece == False:
        janela.tela.blit(alma.image, alma.rect)
    alma.update()
            
    for botao in botoes:
        botao.checaAlma()
        botao.desenhaAcoes()
        botao.acoesMensagem(fonteBatalha)
        botao.mirar(confirmaAtaque)
        botao.batalhaAcontece()
    confirmaAtaque = None
 
    #Esses aqui botei nos comentários pq fico testando a tela de gameover.
    #teclas = pygame.key.get_pressed() 
    #if teclas[pygame.K_w]:
        #y -= 7  
    #if alma.rect.colliderect(caixa):
        #vidaAtual -= 10

    if janela.telaAtual == 'lutaAcontecendo':
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            velocidade = 2.2
        else:
            velocidade = 3.2
        if teclas[pygame.K_RIGHT]:
            x += 1 * velocidade
        if teclas[pygame.K_LEFT]:
            x -= 1  * velocidade
        if teclas[pygame.K_UP]:
            y -= 1 * velocidade
        if teclas[pygame.K_DOWN]:
            y += 1 * velocidade
            
        #Sim, o código está falho ainda. Só tem 1 ataque ai quando acaba fica todo fodido como você pode ver. Eventualmente conserto
        if ataque.mostrar:
            ataque.draw()
            if ataque.contador == 3: #botei isso aqui pra caso o ataque seja resetado pro começo da tela 3 vezes ele parar o ataque e voltar pra tela inicial
                janela.mudarTela('ações')
                janela.atualizaTela()    
            if ataque.atualizar(alma.rect) and ataque.mostrar == False:
                vidaAtual -= 1
                somColisao = pygame.mixer.Sound('assets/sounds/snd_hurt1.wav')
                somColisao.set_volume(0.4)
                somColisao.play()
                janela.mudarTela('ações')
                janela.atualizaTela()
                x = 65
                y = 450

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
    
