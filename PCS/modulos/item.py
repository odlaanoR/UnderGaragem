import pygame
from pygame.locals import *
import modulos.constantes as cos
from modulos.alma import alma

pygame.init()

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
            cos.vidaAtual = min(cos.vidaAtual + 30, cos.vida)
        elif self.nome == 'Cuscuz Paulista':
            cos.vidaAtual -= 1
        if self.quantidade > 0:
            self.quantidade -= 1
        if self.quantidade <= 0 and self in itens:
            itens.remove(self)

    def checaAlma(self):
        if alma.rect.colliderect(self.colisao):
            if self.passou:
                passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                passaAcao.set_volume(0.3)
                passaAcao.play()
                self.passou = False
        else:
            self.passou = True
            
itens = [
    Item('Bolo de Sushi', 'Você recupera 30 de vida'),
    Item('Cuscuz Paulista','NAOOOOOOOOOOOOOOOOOOOOOOO'),
    Item('Comida3','sla3'),
    Item('Comida4','sla4'),
    Item('Comida5','sla5'),
    Item('Comida6','sla6'),
    Item('Comida7','sla7'),
    Item('Comida8','sla8'),
    Item('Comida9','sla9'),
]

print('item carregando...')
