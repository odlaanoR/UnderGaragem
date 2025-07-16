import pygame
from pygame.locals import *
import modulos.constantes as cos

pygame.init()

class Alma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
        pygame.image.load('assets/sprites/alma.png'),
        pygame.image.load('assets/sprites/almaazul.png'),
        pygame.image.load('assets/sprites/almaverde.png'),    
        ]
        self.game_over = pygame.image.load('assets/sprites/almaquebrada.png')
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = cos.x, cos.y
        self.acertavel = True
        self.tempo_inicial = None
        self.tempo_atual = None
        self.gnomo = True

    def update(self):
        self.rect.center = cos.x, cos.y
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))

    def iframe(self):
        global fimInv, tempoInv
        '''if self.gnomo:
            self.tempo_inicial = pygame.time.get_ticks()
            self.gnomo = False
            
        self.tempo_atual = pygame.time.get_ticks()
        print(f'Tempo Atual: {self.tempo_atual}')
        print(f'Tempo Inicial: {self.tempo_inicial}')
        if self.tempo_inicial - self.tempo_atual <= cos.tempoInv:'''
        self.acertavel = False
        pygame.time.set_timer(cos.fimInv, cos.tempoInv, 1)

alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)

print('alma carregando...')
