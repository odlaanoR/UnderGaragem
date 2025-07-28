import pygame
from random import randint
from pygame.locals import *
import modulos.constantes as cos
from modulos.alma import alma
from modulos.ataques import *

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
            cos.vidaAtual = min(cos.vidaAtual + 40, cos.vida)
            cos.cura_som.play()
        elif self.nome == 'Cuscuz Paulista':
            cos.vidaAtual = 1
            cos.dano_snd.play()
        elif self.nome == 'Sopa do Infinito':
            cos.vidaAtual = 92
            cos.cura_som.play()
        elif self.nome == '100 limite':
            if cos.efeito100limite == False:
                cos.efeito100limite = True
                cos.cura_som.play()
                cos.vidaAntes100limite = cos.vidaAtual
                cos.vidaAtual = 100
        elif self.nome == 'Verde':
            cos.vidaAtual = min(cos.vidaAtual + 10, cos.vida)
            cos.cura_som.play()
            alma.estado = 2
            cos.efeitoVerde = True
        elif self.nome == 'BiGaragem':
            cos.vidaAtual = min(cos.vidaAtual + 50, cos.vida)
            cos.cura_som.play()
        elif self.nome == 'MacLanche Infeliz':
            cos.efeitoMcInfeliz = True
            cos.jogador_def += 2
            cos.jogador_atk += 5
            cos.cura_som.play()
        elif self.nome == 'Gororoba Misteriosa':
            cos.cura_som.play()
            vidaAleatoria = randint(0,70)
            cos.vidaAtual = min(cos.vidaAtual + vidaAleatoria, cos.vida)
            print(f'Curou {vidaAleatoria} com A gororoba')
        if self.quantidade > 0:
            self.quantidade -= 1
        if self.quantidade <= 0 and self in itens:
            itens.remove(self)
            '''
        print(f'Usou item: {self.nome}')
        print(f'Vida atual: {cos.vidaAtual} / {cos.vida}')
        print(f'Atk: {cos.jogador_atk} | Def: {cos.jogador_def}')
        print(f'Itens restantes: {[item.nome for item in itens]}')
        '''
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
    Item('Bolo de Sushi', 'Você recupera 40 de vida'),
    Item('Cuscuz Paulista','NAOOOOOOOOOOOOOOOOOOOOOOO'),
    Item('Sopa do Infinito','Você sente como se todas as coisas estivessem equilibradas'),
    Item('100 limite','Você se sente ilimitado (por uma rodada)'),
    Item('Verde','+10 HP Você está verde???????'),
    Item('Gororoba Misteriosa','Cura aleatória. Boa sorte!')
]

print('item carregando...')
