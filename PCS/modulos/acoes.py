import pygame
from pygame.locals import *
import modulos.constantes as cos
from modulos.alma import alma

pygame.init()

class Acao():
    def __init__(self, nome, efeito):
        self.nome = nome
        self.efeito = efeito
        self.colisao = pygame.Rect(0,0,0,0)
        self.passou = False
        
    '''def checaAlma(self):
        if alma.rect.colliderect(self.colisao):
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False
        else:
            self.passou = True'''
      
acoes = [
    Acao('Checar', 'Wilson Tremba, 99 ATK, 99 DEF, o patrão'),
    Acao('Vasculhar', 'Você procura por algo nos arredores...'),
    Acao('Conversar', 'Você tenta dialogar com o Wilson Tremba...'),
    Acao('Implorar por Piedade', 'Você implora por piedade, mas o SEU nome não estava amarelo.')
]   