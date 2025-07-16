import pygame
from modulos.constantes import largura, altura
from pygame.locals import *
pygame.init()

#Essa classe é o que define a largura e altura das janelas. 
class Janelas():
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura,altura))
        self.telaAtual = 'seleções'
        
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
             
class Colisoes():
    def __init__(self, pos_x, pos_y, largura, altura):
        self.rect = pygame.Rect(pos_x, pos_y, largura, altura)
        
    def desenhaColisao(self):
        pygame.draw.rect(janela.tela, (255,0,0), self.rect)
        
janela = Janelas(largura,altura)
colisoes = [
    Colisoes(70, 198, 500, 7), #cima
    Colisoes(76, 190, 7, 175), #esquerda
    Colisoes(70, 356, 500, 7), #baixo
    Colisoes(556, 190, 7, 175), #direita
]
print('janelas carregando...')
