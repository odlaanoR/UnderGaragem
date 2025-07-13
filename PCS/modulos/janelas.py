import pygame
from modulos.constantes import largura, altura
from pygame.locals import *
pygame.init()

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
        
janela = Janelas(largura,altura)
print('janelas carregando...')