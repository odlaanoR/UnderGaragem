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
    print('reiniciando jogo')
    pygame.event.clear()
    reseta_itens()
    reseta_ataques()
    reseta_jogador()
    reseta_botoes()
    cos.dialogo_atual = 0
    cos.usouConversar = 0
    cos.usouVasculhar = 0
    cos.mostraTransicao = False
    cos.acaoSelecionada = None
    cos.usouAcao = False
    cos.musicaFundo = pygame.mixer.music.load('PCS/assets/sounds/Project147.mp3')
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(-1)
    if not cos.zerouJogo:
        cos.musicaFundo = pygame.mixer.music.load('assets/sounds/Project147.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        janela.mudarTela('seleções') 
    else:
        cos.musicaFundo = pygame.mixer.music.load("assets/sounds/[Tremba's Contract].mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        janela.mudarTela('Menu')
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
    global itemSelecionado
    itemSelecionado = None
    if janela.telaAtual == 'inventário' and tecla == K_z:
        for item in itens:
            if alma.rect.colliderect(item.colisao):
                itemSelecionado = item
                janela.mudarTela('transiçãoItens')
                cos.x = 320
                cos.y = 260
                cos.transicaoTempo = pygame.time.get_ticks()
                cos.mostraTransicao = True
                cos.clica_som.set_volume(0.4)
                cos.clica_som.play()
            
def escolheAcao(tecla):
    if janela.telaAtual == 'ações' and tecla == K_z:
        for acao in act.acoes:
            if alma.rect.colliderect(acao.colisao):
                cos.acaoSelecionada = acao
                if acao.nome == 'Conversar':
                    cos.usouConversar += 1
                elif acao.nome == 'Vasculhar':
                    cos.usouVasculhar += 1       
                janela.mudarTela('transiçãoAções')
                cos.x = 320
                cos.y = 260
                cos.transicaoTempo = pygame.time.get_ticks()
                cos.mostraTransicao = True
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
    usouMira()
    if mira < 319:
        precisao = mira/320
        print(precisao)
    elif mira > 321:
        precisao = max(0, 1 - (mira - 320)/320)
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
        else:
            cos.dano_mensagem = 'bloqueado!'
            cos.dano_cor = 'gray'
            cos.dano_tempo = pygame.time.get_ticks()
    else:
        cos.dano_mensagem = 'Errou!'
        cos.dano_cor = 'gray'
        cos.dano_tempo = pygame.time.get_ticks()

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

def usouMira():
    janela.mudarTela('transiçãoMira')
    cos.x = 320
    cos.y = 260
    cos.mostraTransicao = True
    cos.transicaoTempo = pygame.time.get_ticks()

def reseta_rodada(fase):
    for ataque in fase.ataques:
        ataque.resetar()
        #print('ataque resetado')
#Funções para resetar todas as coisas

def reseta_ataques():
    atk.fases = [#0 = alma vermelha; 1 = alma azul; 2 = alma verde
        atk.Gerarataques(atk.rodada1(),),
        atk.Gerarataques(atk.rodada2(),),
        atk.Gerarataques(atk.rodada3(), 2),
        atk.Gerarataques(atk.rodada4(),),
        atk.Gerarataques(atk.rodada5(),),
        atk.Gerarataques(atk.rodada6(), 1),
        atk.Gerarataques(atk.rodada7(), 2),
        atk.Gerarataques(atk.rodada8(), 0, 15),
        atk.Gerarataques(atk.rodada9(), 2, 20),
        atk.Gerarataques(atk.rodada10(), 0,),
        atk.Gerarataques(atk.rodada11(), 1, ),
        atk.Gerarataques(atk.rodada12(), 0, 16),
        atk.Gerarataques(atk.rodada13(), 0)
    ]   
    for fase in atk.fases:
        reseta_rodada(fase)
        
    cos.fase_atual = 0
    cos.ataque_iniciou = False
    cos.ataques_acabaram = False
    
def reseta_jogador():
    cos.vidaAtual = 70
    cos.wilson_vida_atual = 14000

    alma.acertavel = True
    alma.estado = 0

    cos.x = 65
    cos.y = 450
def reseta_itens():
    global itens
    itens = [
        Item('Bolo de Sushi', 'Você recupera 40 de vida'),
        Item('Cuscuz Paulista','NAOOOOOOOOOOOOOOOOOOOOOOO'),
        Item('Sopa do Infinito','Você sente como se todas as coisas estivessem equilibradas'),
        Item('100 limite','Você se sente ilimitado (por uma rodada)'),
        Item('Verde','+10 HP Você está verde???????'),
        Item('BiGaragem','Você recupera 50 de vida'),
        Item('MacLanche Infeliz','De repente, tudo parece uma desgraça. + DEF, +ATK'),
        Item('Gororoba Misteriosa','Cura aleatória. Boa sorte!'),
        Item('O revólver que matou "Felipe"', 'Você equipou essa coisa, você escuta gritos ao seu redor')
    ]

    cos.consumiuItem = False
    cos.efeitoVerde = False
    cos.efeito100limite = False
def reseta_botoes():
    from modulos.selecoes import botoes
    for botao in botoes:
        botao.comecaBatalha = False
        botao.impedeTravaPos = False
        botao.mirando = False
        botao.mostraMsg = False
        botao.passou = False
        botao.gambiarraMsg = pygame.Rect((0,0,0,0))
        botao.x_mira = 40
        
print('inicializando funções...')
