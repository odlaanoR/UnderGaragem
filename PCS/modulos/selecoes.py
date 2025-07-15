import pygame
from pygame.locals import *
import modulos.constantes as cos
from modulos.janelas import janela
from modulos.alma import alma

pygame.init()

class Selecoes(): #to começando a achar que essa classe ta maior doq deveria mas fazer oq
    corPadrao = (150,75,0)
    novaCor = (255,255,0)
    def __init__(self, pos_x, msg): 
        self.botao = pygame.Rect(pos_x, 430, 100, 40)
        self.cor = self.corPadrao
        self.mostraMsg = False #é o que confirma se o texto quando clicar nos botões deve ou não aparecer
        self.mensagem = msg #é o texto que aparece quando clica em algum dos botões de seleções
        self.passou = False
        self.gambiarraMsg = pygame.Rect((0,0,0,0)) #ah, esqueci de explicar. Isso aqui foi uma variável que eu criei pq queria que o texto lá das seleções fossem clicáveis (talvez tenha um jeito melhor de fazer isso)
        self.mira = pygame.Rect((0,0,0,0))
        self.x_mira = 40
        self.mirando = False
        self.comecaBatalha = False #isso indica se a batalha deve ou não começar
        self.impedeTravaPos = False #e esse aqui impede que o x e o y do jogador seja resetado. EU N AGUENTO MAIS (não pensei em um nome melhor)
        self.comecoMira = 0 #tive que criar isso aqui pq a mira tava selecionando automaticamente
        
    def desenhaSelecoes(self):
        pygame.draw.rect(janela.tela, self.cor, self.botao, width=2)

    #Serve para checar se a alma passou por algum botão, se sim, toca um som
    def checaAlma(self): 
        if alma.rect.colliderect(self.botao):
            self.cor = self.novaCor
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False   
        else:
            self.cor = self.corPadrao
            self.passou = True
            
    def checaClique(self, tecla):
        if tecla == K_z and alma.rect.colliderect(self.botao):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.mp3')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.gambiarraMsg = pygame.Rect(30, 215, 10, 10)
            if self.mensagem == 'Item':
                global x, y
                cos.x = 155
                cos.y = 220
                janela.mudarTela('inventário')
                self.mostraMsg = False
            elif self.mensagem == 'Checar':
                cos.x = 40
                cos.y = 220
                janela.mudarTela('ações')
                self.mostraMsg = False
            else:
                self.mostraMsg = True
    def mirar(self, tecla):
        global tempoAtual
        if self.mirando:
            print('mirar inicia')
            self.alvo = pygame.image.load('assets/sprites/mira.png')
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
                self.impedeTravaPos = False
                print(self.comecaBatalha)
                print(self.impedeTravaPos)
        
    #Método que, quando chamado, muda o jogador para a tela de combate. O comecaBatalha (flag) serve para garantir que a função não seja chamada até que a flag seja verdadeira
    def batalhaAcontece(self):
        global x, y, tempoLuta
        if self.comecaBatalha and self.impedeTravaPos == False:
            tempoLuta = pygame.time.get_ticks()
            janela.mudarTela('lutaAcontecendo')
            cos.x = 320
            cos.y = 260
            self.impedeTravaPos = True
            print('batalha acontece')
                    
    def confirmaSelecao(self, tecla):
        if self.mostraMsg and tecla == K_z and alma.rect.colliderect(self.gambiarraMsg):
            clicaAcao = pygame.mixer.Sound('assets/sounds/snd_select.mp3')
            clicaAcao.set_volume(0.4)
            clicaAcao.play()
            self.mostraMsg = False
            return True
        return False

    def cancelaSelecao(self):
        self.mostraMsg = False
            
    def selecaoMensagem(self, fonte):
        if self.mostraMsg:
            janela.tela.blit(fonte.render(self.mensagem, True, (255,255,255)), (43,205))

    def confirmaLuta(self):
        self.mirando = True
        self.comecoMira = pygame.time.get_ticks()
        
    def confirmaAgir(self):
        janela.mudarTela('ações')
        print('poggers')
        
    def confirmaTelaItem(self):
        janela.mudarTela('inventário')
            
    def confirmaPiedade(self):
        print('Mas não estava amarelo')
        
botoes = [
    Selecoes(50, "Wilson Tremba"),
    Selecoes(190, "Checar"),
    Selecoes(330, "Item"),
    Selecoes(470, "Piedade"),
    ]

print('inicializando seleções')
