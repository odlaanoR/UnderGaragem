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
        self.contadorEfeito = 0
        
    def checaAlma(self):
        if alma.rect.colliderect(self.colisao):
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False
        else:
            self.passou = True
            
acoes = [
    Acao('Checar', 'Wilson Tremba, 99 ATK, 99 DEF, o patrão'),
    Acao('Vasculhar', ''),
    Acao('Conversar', ''),
    Acao('Implorar por Piedade', 'Mas o SEU nome não estava amarelo.')
]   
