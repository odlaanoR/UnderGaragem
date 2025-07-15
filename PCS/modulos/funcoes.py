import pygame
from pygame.locals import *
from modulos.janelas import janela
from modulos.selecoes import *
from modulos.item import *
from modulos.alma import alma
import modulos.ataques as atk
import modulos.acoes as act
import modulos.constantes as cos

escudo = pygame.draw.line(janela.tela, 'blue', (0,0), (0,0), 1)
itemSelecionado = None
consumiuItem = False
#Essa função serve para reiniciar tudo que já aconteceu, então se, por exemplo, o jogador já tiver usado um item e ele morre na batalha, a função é chamada e restaura todos os itens dele.
def reiniciar_jogo():
    global vidaAtual, gameover, x, y, musicaFundo, itens, fase_atual, ataque_iniciou, fases, usouConversar, usouVasculhar
    cos.vidaAtual = 70
    cos.x = 65
    cos.y = 450
    gameover = False
    cos.usouConversar = 0
    cos.usouVasculhar = 0
    cos.fase_atual = 0
    cos.ataque_iniciou = False
    musicaFundo = pygame.mixer.music.load('assets/sounds/Project147.mp3')
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
    print('reiniciando jogo')
    fases = [
        atk.Gerarataques(atk.rodada1(), 10),
        atk.Gerarataques(atk.rodada2(), 10)
    ]
#Quando a função é chamada, digita todos os textos dos itens na tela (de forma organizada). Além de criar a colisão nos itens inscritos na tela (junto com o gambiarra (definido no módulo de seleções))   
def printaItens():
    iy = 0
    ix = 0
    colisaoItens = []
    for item in itens:
        if iy <= 3:
            posicaoItem = (170 + ix * 200, 205 + iy * 35)
            item.colisao = pygame.Rect(posicaoItem[0] - 20, posicaoItem[1] + 10, 50, 10) 
            colisaoItens.append(item.colisao)
            janela.escreveTexto(f'{item.nome}', cos.fonteBatalha, (255,255,255), posicaoItem)
            if alma.rect.colliderect(botoes[2].gambiarraMsg):
                botoes[2].mostraMsg = True
            iy += 1
        else:
            iy = 0
            ix += 1

#Se o jogador estiver na tela do inventário e confirmar a ação (clicando no Z) estando em colisao com qualquer item, ele será redirecionado para a tela que confirma qual item ele usou e o efeito que ele faz.
def consomeItem(tecla):
    global itemSelecionado, consumiuItem, mostraTransicao, transicaoTempo
    if janela.telaAtual == 'inventário' and tecla == K_z:
        for item in itens:
            if alma.rect.colliderect(item.colisao):
                itemSelecionado = item
                janela.mudarTela('transiçãoItens')
                transicaoTempo = pygame.time.get_ticks()
                mostraTransicao = True
                cos.clica_som.set_volume(0.4)
                cos.clica_som.play() 
                
def printaAcoes():
    ix = 0
    iy = 0
    colisaoAcoes = []
    for acao in act.acoes:
        if iy <= 1:
            posicaoAcao = (55 + ix * 200, 205 + iy * 35)
            acao.colisao = pygame.Rect(posicaoAcao[0] - 20, posicaoAcao[1] + 10, 50, 10)
            colisaoAcoes.append(acao.colisao)
            janela.escreveTexto(f'{acao.nome}', cos.fonteBatalha, (255,255,255), posicaoAcao)
            iy += 1
        else:
            iy = 0
            ix += 1
            posicaoAcao = (55 + ix * 200, 205 + iy * 35)
            acao.colisao = pygame.Rect(posicaoAcao[0] - 20, posicaoAcao[1] + 10, 50, 10)
            colisaoAcoes.append(acao.colisao)
            janela.escreveTexto(f'{acao.nome}', cos.fonteBatalha, (255,255,255), posicaoAcao)
            iy += 1
            
def escolheAcao(tecla):
    global acaoSelecionada, usouAcao, mostraTransicao, transicaoTempo
    acaoSelecionada = None
    usouAcao = False
    if janela.telaAtual == 'ações' and tecla == K_z:
        for acao in act.acoes:
            if alma.rect.colliderect(acao.colisao):
                acaoSelecionada = acao
                if acao.nome == 'Conversar':
                    cos.usouConversar += 1
                elif acao.nome == 'Vasculhar':
                    cos.usouVasculhar += 1       
                janela.mudarTela('transiçãoAções')
                transicaoTempo = pygame.time.get_ticks()
                mostraTransicao = True
                cos.clica_som.set_volume(0.4)
                cos.clica_som.play()

def verde():
    global escudo
    if cos.direcao == "cima":
        escudo = pygame.draw.line(janela.tela, 'green', ((janela.tela.get_width()/2)-50, (janela.tela.get_height()/2)-50), ((janela.tela.get_width()/2)+50, (janela.tela.get_height()/2)-50), 4)
        return escudo
    elif cos.direcao == "baixo":
        escudo = pygame.draw.line(janela.tela, 'yellow', ((janela.tela.get_width()/2)-50, (janela.tela.get_height()/2)+50), ((janela.tela.get_width()/2)+50, (janela.tela.get_height()/2)+50), 4)
        return escudo
    elif cos.direcao == "esquerda":
        escudo = pygame.draw.line(janela.tela, 'red', ((janela.tela.get_width()/2)-50, (janela.tela.get_height()/2)+50), ((janela.tela.get_width()/2)-50, (janela.tela.get_height()/2)-50), 4)
        return escudo
    elif cos.direcao == "direita":
        escudo = pygame.draw.line(janela.tela, 'blue', ((janela.tela.get_width()/2)+50, (janela.tela.get_height()/2)+50), ((janela.tela.get_width()/2)+50, (janela.tela.get_height()/2)-50), 4)
        return escudo
                
print('inicializando funções...')
