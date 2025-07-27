import pygame
from pygame.locals import *
import modulos.constantes as cos

pygame.init()

class Alma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
        pygame.image.load('PCS/assets/sprites/alma.png'),
        pygame.image.load('PCS/assets/sprites/almaazul.png'),
        pygame.image.load('PCS/assets/sprites/almaverde.png'),    
        ]
        self.game_over = pygame.image.load('PCS/assets/sprites/almaquebrada.png')
        self.estado = 0
        self.image = self.sprites[self.estado]
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = cos.x, cos.y
        self.acertavel = True
        self.tempo_inicial = None
        self.tempo_atual = None
        #self.gnomo = True

    def update(self):
        self.rect.center = cos.x, cos.y
        if self.acertavel == False:
            self.image = pygame.image.load('PCS/assets/sprites/almavazia.png')
        else:
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

    def trocaestado(self, novoestado=0):#auto explicativo
        if novoestado == '+':
            self.estado += 1
        else:
            self.estado = int(novoestado)

alma = Alma()
artes = pygame.sprite.Group()
artes.add(alma)

class Wilson(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.wilsonsprites = []
        for i in range(3):
            img = cos.wilsonsheet.subsurface((i * 150, 0), (150,150))
            img = pygame.transform.scale(img, (190, 190))
            self.wilsonsprites.append(img)
            
        self.indexWilson = 0
        self.image = self.wilsonsprites[self.indexWilson]
        self.rect = self.image.get_rect()
        self.rect.center = 300, 85
        
    def update(self):
        self.indexWilson += 0.013
        if self.indexWilson >= len(self.wilsonsprites):
            self.indexWilson = 0
        self.image = self.wilsonsprites[int(self.indexWilson)]

wilson_sprite = Wilson()
artes.add(wilson_sprite)

class AnimacaoAtaque(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_ataque = []
        for i in range(4):
            img = cos.sprite_sheet.subsurface((0, i * 88), (38,88))
            img = pygame.transform.scale(img, (38 * 2, 88*2))
            self.imagens_ataque.append(img)

        self.indexLista = 0
        self.image = self.imagens_ataque[self.indexLista]
        self.rect = self.image.get_rect()
        self.rect.center = (290,68)
        
    def update(self):
        self.indexLista += 0.07
        if self.indexLista >= len(self.imagens_ataque):
            self.indexLista = 0
        self.image = self.imagens_ataque[int(self.indexLista)]
    
    
ataques_sprite = AnimacaoAtaque()
artes.add(ataques_sprite)
print('alma carregando...')
