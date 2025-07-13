import pygame
from pygame.locals import *
from modulos.janelas import janela
from modulos.selecoes import *
from modulos.item import *
from modulos.alma import alma
from modulos.ataques import *
import modulos.constantes as cos

def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo, itens, ataque, ataque2, ataque3
    cos.vidaAtual = 70
    cos.x = 65
    cos.y = 450
    gameover = False
    musicaFundo = pygame.mixer.music.load('assets/Project147.mp3')
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(-1)
    janela.mudarTela('seleções')
    itens = [
        Item('Bolo de Sushi', 'Você recupera 30 de vida'),
        Item('Cuscuz Paulista','brutal'),
        Item('Comida3','sla3'),
        Item('Comida4','sla4'),
        Item('Comida5','sla5'),
        Item('Comida6','sla6'),
        Item('Comida7','sla7'),
        Item('Comida8','sla8'),
        Item('Comida9','sla9'),
    ]
    ataque = Ataque((255,255,255), 80, 220, 20, 20, 3, 0, 5) #o ataque não volta depois do gameover (ajeitar isso depois)
    ataque2 = Ataque('white', 90, 250, 40, 40, 10, 0, 5)
    ataque3 = Ataque('red', 150, 150, 30, 30, 0, 0, 0)
        
def printaItens():
    iy = 0
    ix = 0
    colisaoItens = []
    for item in itens:
        if iy <= 3:
            posicaoItem = (170 + ix * 200, 205 + iy * 35)
            item.colisao = pygame.Rect(posicaoItem[0] - 20, posicaoItem[1] + 10, 50, 10) #isso aqui foi uma das coisas mais absurdas que o gpt me ajudou
            colisaoItens.append(item.colisao)
            janela.escreveTexto(f'{item.nome}', cos.fonteBatalha, (255,255,255), posicaoItem)
            if alma.rect.colliderect(botoes[2].gambiarraMsg):
                botoes[2].mostraMsg = True
            iy += 1
        else:
            iy = 0
            ix += 1
            
def consomeItem(tecla):
    global itemSelecionado, consumiuItem, mostraTransicao, transicaoTempo
    itemSelecionado = None
    consumiuItem = False
    if janela.telaAtual == 'inventário' and tecla == K_z:
        for item in itens:
            if alma.rect.colliderect(item.colisao):
                itemSelecionado = item
                janela.mudarTela('transiçãoItens')
                consumiuItem = True
                transicaoTempo = pygame.time.get_ticks()
                mostraTransicao = True
                clicaItem = pygame.mixer.Sound('assets/sounds/snd_select.wav')
                clicaItem.set_volume(0.4)
                clicaItem.play()
                
print('inicializando funções...')
