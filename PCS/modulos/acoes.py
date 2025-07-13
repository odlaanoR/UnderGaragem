import pygame
from pygame.locals import *
import modulos.constantes as cos
from modulos.janelas import janela
from modulos.item import itens
from modulos.alma import alma
global contadorTurno

contadorTurno = 0
pygame.init()

class Acoes(): #to começando a achar que essa classe ta maior doq deveria mas fazer oq
    corPadrao = (150,75,0)
    novaCor = (255,255,0)
    def __init__(self, pos_x, msg): 
        self.botao = pygame.Rect(pos_x, 430, 100, 40)
        self.cor = self.corPadrao
        self.mostraMsg = False #é o que confirma se o texto quando clicar nos botões deve ou não aparecer
        self.mensagem = msg #é o texto que aparece quando clica em algum dos botões de ações
        self.passou = False
        self.gambiarraMsg = pygame.Rect((0,0,0,0)) #ah, esqueci de explicar. Isso aqui foi uma variável que eu criei pq queria que o texto lá das ações fossem clicáveis (talvez tenha um jeito melhor de fazer isso)
        self.mira = pygame.Rect((0,0,0,0))
        self.x_mira = 40
        self.mirando = False
        self.comecaBatalha = False #isso indica se a batalha deve ou não começar
        self.impedeTravaPos = False #e esse aqui impede que o x e o y do jogador seja resetado. EU N AGUENTO MAIS (não pensei em um nome melhor)
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
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.gambiarraMsg = pygame.Rect(30, 215, 10, 10)
            if self.mensagem == 'Item':
                global x, y
                cos.x = 155
                cos.y = 220
                janela.mudarTela('inventário') 
            else:
                self.mostraMsg = True
    def mirar(self, tecla):
        global tempoAtual
        if self.mirando:
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
        global x, y, tempoLuta, contadorTurno
        contadorTurno = 0
        if self.comecaBatalha and self.impedeTravaPos == False:
            tempoLuta = pygame.time.get_ticks()
            janela.mudarTela('lutaAcontecendo')
            cos.x = 320
            cos.y = 260
            self.impedeTravaPos = True
            contadorTurno += 1
            
    def confirmaAcao(self, tecla):
        if self.mostraMsg and tecla == K_z and alma.rect.colliderect(self.gambiarraMsg):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.wav')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.mostraMsg = False
            return True
        return False

    def cancelaAcao(self):
        self.mostraMsg = False
            
    def acoesMensagem(self, fonte):
        if self.mostraMsg:
            janela.tela.blit(fonte.render(self.mensagem, True, (255,255,255)), (43,205))

    def confirmaLuta(self):
        self.mirando = True
        self.comecoMira = pygame.time.get_ticks()
        
    def confirmaAgir(self):
        print('poggers')
        
    def confirmaTelaItem(self):
        janela.mudarTela('inventário')
            
    def confirmaPiedade(self):
        print('Mas não estava amarelo')
        
class Item():
    def __init__(self, nome, descricao, quantidade=1):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.colisao = pygame.Rect(0,0,0,0)
        self.passou = False
        
    def usar(self):
        global vidaAtual
        if self.nome == 'Bolo de Sushi': 
            vidaAtual = min(vidaAtual + 30, cos.vida)
        elif self.nome == 'Cuscuz Paulista':
            vidaAtual -= 1
        if self.quantidade > 0:
            self.quantidade -= 1
        if self.quantidade <= 0 and self in itens:
            itens.remove(self)

    def checaAlma(self):
        if alma.rect.colliderect(self.colisao):
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.wav')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False
        else:
            self.passou = True
            
botoes = [
    Acoes(50, "Wilson Tremba"),
    Acoes(190, "Checar"),
    Acoes(330, "Item"),
    Acoes(470, "Piedade"),
    ]

print('inicializando ações')