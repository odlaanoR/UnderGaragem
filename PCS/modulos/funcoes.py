import pygame
from pygame.locals import *
from modulos.janelas import janela
from modulos.selecoes import *
from modulos.item import *
from modulos.alma import alma
import modulos.acoes as act
import modulos.ataques as atk
from modulos.ataques import *
import modulos.constantes as cos

escudo = pygame.draw.line(janela.tela, 'blue', (0,0), (0,0), 1)

#Essa função serve para reiniciar tudo que já aconteceu, então se, por exemplo, o jogador já tiver usado um item e ele morre na batalha, a função é chamada e restaura todos os itens dele.
def reiniciarJogo():
    global vidaAtual, vida, gameover, x, y, musicaFundo, itens, fase_atual, ataque_iniciou, fases, eventos, usouConversar, usouVasculhar
    cos.vidaAtual = 70
    cos.vida = 92
    cos.x = 65
    cos.y = 450
    gameover = False
    eventos = pygame.event.get()
    cos.fase_atual = 0
    cos.ataque_iniciou = False
    cos.usouConversar = 0
    cos.usouVasculhar = 0
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
        atk.Gerarataques(atk.rodada2(), 10),
        atk.Gerarataques(atk.rodada3(), 10)
    ]
    alma.acertavel = True
    for evento in eventos:
        for botao in botoes:      
            if evento.type == cos.fim_do_ataque and janela.telaAtual == 'lutaAcontecendo':#Encerra o turno de ataque inimigo
                ataque.mostrar = True
                janela.mudarTela('seleções')
                cos.x = 65
                cos.y = 450
                #print("fim do ataque")
                botao.impedeTravaPos = False
                botao.comecaBatalha = False
                cos.fase_atual += 1  
#Quando a função é chamada, digita todos os textos dos itens na tela (de forma organizada). Além de criar a colisão nos itens inscritos na tela (junto com o gambiarra (definido no módulo de seleções))   
def printaItens(botoes):
    iy = 0
    ix = 0
    colisaoItens = []
    for item in itens:
        if iy < 4:
            posicaoItem = (175 + ix * 200, 215 + iy * 35)
            item.colisao = pygame.Rect(posicaoItem[0] - 20, posicaoItem[1] + 10, 50, 10) 
            colisaoItens.append(item.colisao)
            janela.escreveTexto(f'{item.nome}', cos.fonteBatalha, (255,255,255), posicaoItem)
            if alma.rect.colliderect(botoes[2].gambiarraMsg):
                botoes[2].mostraMsg = True
            iy += 1
        else:
            iy = 0
            ix += 1
            posicaoItem = (175 + ix * 200, 215 + iy * 35)
            item.colisao = pygame.Rect(posicaoItem[0] - 20, posicaoItem[1] + 10, 50, 10) 
            colisaoItens.append(item.colisao)
            janela.escreveTexto(f'{item.nome}', cos.fonteBatalha, (255,255,255), posicaoItem)
            iy += 1
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
            
#Se o jogador estiver na tela do inventário e confirmar a ação (clicando no Z) estando em colisao com qualquer item, ele será redirecionado para a tela que confirma qual item ele usou e o efeito que ele faz.
def consomeItem(tecla):
    global itemSelecionado, consumiuItem, mostraTransicao, transicaoTempo
    itemSelecionado = None
    consumiuItem = False
    if janela.telaAtual == 'inventário' and tecla == K_z:
        for item in itens:
            if alma.rect.colliderect(item.colisao):
                itemSelecionado = item
                janela.mudarTela('transiçãoItens')
                transicaoTempo = pygame.time.get_ticks()
                mostraTransicao = True
                cos.clica_som.set_volume(0.4)
                cos.clica_som.play()
            
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
        escudo = pygame.draw.line(janela.tela, 'green', ((janela.tela.get_width()/2)-30, (janela.tela.get_height()/2)-30), ((janela.tela.get_width()/2)+30, (janela.tela.get_height()/2)-30), 4)
        return escudo
    elif cos.direcao == "baixo":
        escudo = pygame.draw.line(janela.tela, 'yellow', ((janela.tela.get_width()/2)-30, (janela.tela.get_height()/2)+30), ((janela.tela.get_width()/2)+30, (janela.tela.get_height()/2)+30), 4)
        return escudo
    elif cos.direcao == "esquerda":
        escudo = pygame.draw.line(janela.tela, 'red', ((janela.tela.get_width()/2)-30, (janela.tela.get_height()/2)+30), ((janela.tela.get_width()/2)-30, (janela.tela.get_height()/2)-30), 4)
        return escudo
    elif cos.direcao == "direita":
        escudo = pygame.draw.line(janela.tela, 'blue', ((janela.tela.get_width()/2)+30, (janela.tela.get_height()/2)+30), ((janela.tela.get_width()/2)+30, (janela.tela.get_height()/2)-30), 4)
        return escudo
    
def ataque_player(mira):

    if mira < 300:
        precisao = mira/300
        print(precisao)
    elif mira > 300:
        precisao = max(0, 1 - (mira - 300)/300)
        print(precisao)
    else:
        precisao = 1.5
        print("critico!")
    
    if precisao != 0:
        if cos.jogador_atk >= cos.wilson_def:
            cos.dano_mensagem = str(round(cos.jogador_atk + (cos.jogador_atk*(precisao*2))))
            cos.wilson_vida_atual -= int(cos.dano_mensagem)
            cos.dano_cor = 'red'
            cos.dano_tempo = pygame.time.get_ticks()
            print(cos.dano_mensagem)
            mostraTransicao = True
        else:
            cos.dano_mensagem = 'bloqueado!'
            cos.dano_cor = 'gray'
            cos.dano_tempo = pygame.time.get_ticks()
            mostraTransicao = True

    else:
        cos.dano_mensagem = 'Errou!'
        cos.dano_cor = 'gray'
        cos.dano_tempo = pygame.time.get_ticks()
        mostraTransicao = True


def mostrarDano():
    if cos.dano_mensagem:
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - cos.dano_tempo < 1500:  # mostra por 1.5 segundos
            janela.escreveTexto(cos.dano_mensagem, cos.fonteBatalha, cos.dano_cor, (janela.tela.get_width()/2, janela.tela.get_height()/2 - 150))
        else:
            # Limpa a mensagem após o tempo
            cos.dano_mensagem = None
        pygame.draw.rect(janela.tela, 'red', ((janela.tela.get_width()/2-150, janela.tela.get_height()/2 - 100), (1*(cos.wilson_vida_max/50), 20)))
        pygame.draw.rect(janela.tela, 'green', ((janela.tela.get_width()/2-150, janela.tela.get_height()/2 - 100), (1*(cos.wilson_vida_atual/50), 20)))


                
print('inicializando funções...')