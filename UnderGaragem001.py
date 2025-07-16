import pygame
from pygame.locals import *
from modulos.alma import alma
from modulos.janelas import *
from modulos.selecoes import *
from modulos.item import *
import modulos.ataques as atk
import modulos.funcoes as func
import modulos.constantes as cos
import modulos.acoes as act
from sys import exit

fases = [
    atk.Gerarataques(atk.rodada1(), 10),
    atk.Gerarataques(atk.rodada2(), 10),
    atk.Gerarataques(atk.rodada3(), 10)
]

while True:
    cos.fps.tick((60))
    pygame.display.update()
    eventos = pygame.event.get()
    confirmaAtaque = None
    
    
    for evento in eventos:
        #detecta se o tipo do evento é quando o jogador pressiona e solta rapidamente uma tecla
        if evento.type == KEYDOWN:
            if evento.key == K_j: #debug de mudar o estado das almas
                alma.estado += 1
                print("trocando estado")
                if alma.estado >= len(alma.sprites):
                    alma.estado = 0
            '''elif evento.key == K_p: #debug de passar as rodadas
                cos.fase_atual += 1'''
                    
        #Detecta se houve o KEYDOWN na tela de seleções        
        if evento.type == KEYDOWN and janela.telaAtual == 'seleções':
            confirmaAtaque = evento.key
            if evento.key == K_RIGHT and not alma.rect.colliderect(botoes[3].botao) and not any(botao.mostraMsg for botao in botoes):
                cos.x += 140
            if evento.key == K_LEFT and not alma.rect.colliderect(botoes[0].botao) and not any(botao.mostraMsg for botao in botoes):
                cos.x -= 140
        
            #Detecta se houve algum evento nos botões de seleções (Lutar, Agir, Item, Poupar)
            if evento.key == K_z:
                cos.x = 30
                cos.y = 220
                for botao in botoes:
                    botao.checaClique(evento.key)
                if botoes[0].confirmaSelecao(evento.key):
                    botoes[0].confirmaLuta()
                    botoes[0].batalhaAcontece()
                if botoes[1].confirmaSelecao(evento.key):
                    botoes[1].confirmaAgir()
                if botoes[2].confirmaSelecao(evento.key):
                    botoes[2].confirmaTelaItem()
                if botoes[3].confirmaSelecao(evento.key):
                    botoes[3].confirmaPiedade()

            if evento.key == K_x and not any(botao.mirando for botao in botoes):
                for botao in botoes:
                    botao.cancelaSelecao()
                cos.x = 65
                cos.y = 450
         
        #Eventos detectados após o jogador selecionar o botão de Agir      
        if evento.type == KEYDOWN and janela.telaAtual == 'ações':
            if evento.key == K_RIGHT:
                if alma.rect.colliderect(act.acoes[0].colisao) or alma.rect.colliderect(act.acoes[1].colisao):
                    cos.x += 200
            if evento.key == K_LEFT:
                if alma.rect.colliderect(act.acoes[2].colisao) or alma.rect.colliderect(act.acoes[3].colisao):
                    cos.x -= 200
            if evento.key == K_DOWN:
                if alma.rect.colliderect(act.acoes[0].colisao) or alma.rect.colliderect(act.acoes[2].colisao):
                    cos.y += 35
            if evento.key == K_UP:
                if alma.rect.colliderect(act.acoes[1].colisao) or alma.rect.colliderect(act.acoes[3].colisao):
                    cos.y -= 35     
            if evento.key == K_z:
                func.escolheAcao(evento.key)
            if evento.key == K_x:
                janela.mudarTela('seleções')
                cos.x = 65
                cos.y = 450
                
        #Eventos detectados após o jogador selecionar "Item"         
        if evento.type == KEYDOWN and janela.telaAtual == 'inventário': 
            if evento.key == K_DOWN:
                cos.y += 35
            if evento.key == K_UP:
                cos.y -= 35
            if evento.key == K_RIGHT:
                cos.x += 200
            if evento.key == K_LEFT:
                cos.x -= 200
            if evento.key == K_z:
                func.consomeItem(evento.key)
            if evento.key == K_x:
                janela.mudarTela('seleções')
                cos.x = 65
                cos.y = 450
                             
        if evento.type == KEYDOWN and janela.telaAtual == 'piedade':
            if evento.key == K_z:
                func.mostraTransicao = True
                func.transicaoTempo = pygame.time.get_ticks()
                
        if evento.type == QUIT:
            pygame.quit()
            exit()
               
        for botao in botoes:      
            if evento.type == cos.fim_do_ataque and janela.telaAtual == 'lutaAcontecendo':#Encerra o turno de ataque inimigo
                ataque.mostrar = True
                janela.mudarTela('seleções')
                cos.x = 65
                cos.y = 450
                print("fim do ataque")
                botao.impedeTravaPos = False
                botao.comecaBatalha = False
                cos.fase_atual += 1  

        if evento.type == cos.fimInv:
            alma.acertavel = True
            print("Iframe off")
            
    #Tela de seleções    
    janela.corFundo()
    janela.escreveTexto(f'HP:{cos.vidaAtual}/{cos.vida}', cos.fonte, (255,255,255),(260,385))
    janela.escreveTexto('Lutar', cos.fonteCustomizada, botoes[0].cor, (85, 433))
    janela.escreveTexto('Agir', cos.fonteCustomizada, botoes[1].cor, (238, 433))
    janela.escreveTexto('Item', cos.fonteCustomizada, botoes[2].cor, (373, 433))
    janela.escreveTexto('Poupar', cos.fonteCustomizada, botoes[3].cor, (495, 433))
    
    if cos.fase_atual == 2 and janela.telaAtual == 'seleções':
        janela.escreveTexto('o próximo ataque utiliza uma mecanica diferente', cos.fonteCustomizada, 'white', (50, (janela.tela.get_height()/2)))
        janela.escreveTexto('use as setinhas para se defender', cos.fonteCustomizada, 'white', (50, (janela.tela.get_height()/2+40)))
    elif cos.fase_atual == 3:
        janela.escreveTexto('a demo acaba aqui! aja denovo para crachar o jogo :D', cos.fonteCustomizada, 'white', (50, (janela.tela.get_height()/2)))
        
    #vida em barra
    vida_max_barra = pygame.draw.rect(janela.tela, 'red', (370,395, (1*cos.vida), 20))
    vida_atual_barra = pygame.draw.rect(janela.tela, 'green', (370,395, (1*cos.vidaAtual), 20))

    #Desenha as Caixas
    if janela.telaAtual == 'lutaAcontecendo' or janela.telaAtual == 'inventário':
        janela.desenhaCaixa((70, 190, 500, 180))
    else:
        janela.desenhaCaixa((10,180,620,180))
        
    almaDesaparece = any(botao.mirando for botao in botoes) or janela.telaAtual == 'transiçãoItens' or janela.telaAtual == 'transiçãoAções' or janela.telaAtual == 'piedade'

    if almaDesaparece == False:
        janela.tela.blit(alma.image, alma.rect)
    alma.update()
            
    for botao in botoes:
        botao.checaAlma()
        botao.desenhaSelecoes()
        botao.selecaoMensagem(cos.fonteBatalha)
        botao.mirar(confirmaAtaque)
        botao.batalhaAcontece()
    confirmaAtaque = None
    
    #Tela de Luta
    if botoes[0].comecaBatalha and janela.telaAtual == 'lutaAcontecendo':
        '''for colisao in colisoes:
            if alma.rect.colliderect(colisao.rect):
                print('bateu')'''
        if alma.estado == 1:
            cos.y += 1
            pygame.display.set_caption("Você está azul agora!")
        elif alma.estado == 2:
            cos.x = janela.tela.get_width() / 2
            cos.y = janela.tela.get_height() / 2
            velocidade = 0
            func.verde()
            pygame.display.set_caption("Você está verde!")
        else:
            pygame.display.set_caption("Você se enche de DETERMINAÇÃO")
            velocidade = 3.2
      
        #Na tela de luta acontecendo, o jogador passa a se mover continuamente quando pressiona e segura uma tecla, o que faz essa detecção é essa variável teclas que recebe a função do pygame get_pressed
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            velocidade = 2.7
        if teclas[pygame.K_RIGHT] and not alma.rect.colliderect(colisoes[3].rect):
            cos.x += 1 * velocidade
            cos.direcao = 'direita'
        if teclas[pygame.K_LEFT] and not alma.rect.colliderect(colisoes[1].rect):
            cos.x -= 1  * velocidade
            cos.direcao = 'esquerda'
        if teclas[pygame.K_UP] and not alma.rect.colliderect(colisoes[0].rect):
            cos.y -= 1 * velocidade
            cos.direcao = 'cima'
        if teclas[pygame.K_DOWN] and not alma.rect.colliderect(colisoes[2].rect):
            cos.y += 1 * velocidade
            cos.direcao = 'baixo'

        fase = fases[cos.fase_atual]#declara a fase atual
        if cos.fase_atual == 2:
            alma.estado = 2
        if not cos.ataque_iniciou: #criado para os temporizados funcionarem de maneira apropriada
            pygame.time.set_timer(cos.fim_do_ataque, 5000)
            for ataque in fase.ataques:#Tentativa de fazer os delays funcionarem, estado bem inicial(não funciona)
                ataque.iniciar()
            cos.ataque_iniciou = True
            #print("Todos os ataques foram iniciados")

        for ataque in fase.ataques: #gera os ataques baseado na rodada
            resultado = ataque.atualizar(alma, func.escudo, alma.estado)
            #print("ataque atualizar foi chamado")
            if ataque.mostrar:
                ataque.draw(janela.tela)
            if resultado == "dano" and not ataque.mostrar:
                cos.vidaAtual -= 10
                cos.dano_snd.play()
                alma.iframe()
                print('deu dano')
            elif resultado == "parry" and not ataque.mostrar:
                cos.parry_snd.play()
                print('deu parry')          
                
    #Tela de Agir
    if janela.telaAtual == 'ações':   
        func.printaAcoes()
        for acao in act.acoes:
            acao.checaAlma()
                
    #Na tela de ações,            
    if janela.telaAtual == 'transiçãoAções':
        acao = func.acaoSelecionada
        if acao.nome == 'Conversar':
            if cos.usouConversar == 1:
                textoEfeito = 'Você tenta dialogar com o Wilson Tremba...'
                texto2 = 'Mas ele não respondeu'
            elif cos.usouConversar == 2:
                textoEfeito = 'Wilson Tremba se tremeu ao você elogiar seu relógio.'
                texto2 = ''
            elif cos.usouConversar == 3:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
        elif acao.nome == 'Vasculhar':
            if cos.usouVasculhar == 1:
                textoEfeito = 'Você olha ao seu redor em busca de algo que'
                texto2 = 'possa lhe ajudar... Nada'
            elif cos.usouVasculhar == 2:
                textoEfeito = 'Você achou um rato, ele faz barulho'
                texto2 = ''       
        elif acao.nome == 'Checar':
            textoEfeito = acao.efeito
            texto2 = ''
        elif acao.nome == 'Implorar por Piedade':
            textoEfeito = acao.efeito
            texto2 = ''
            
        janela.escreveTexto(textoEfeito, cos.fonteBatalha, (255,255,255), (50,220))  
        janela.escreveTexto(texto2, cos.fonteBatalha, (255,255,255), (50,250))
              
        if func.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - func.transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                        
    #Tela de Inventário
    if janela.telaAtual == 'inventário':
        func.printaItens()
        for item in itens:
            item.checaAlma()
            
    if janela.telaAtual == 'transiçãoItens':
        janela.escreveTexto(f'Você usou {func.itemSelecionado.nome}', cos.fonteBatalha, (255,255,255), (90,230))
        janela.escreveTexto(f'{func.itemSelecionado.descricao}', cos.fonteBatalha, (255,255,255), (90,260)) 
         
        if not func.consumiuItem:
            func.itemSelecionado.usar()
            func.consumiuItem = True
        if func.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - func.transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
    
    #Tela de Piedade
    if janela.telaAtual == 'piedade':
        janela.escreveTexto('Mas não estava amarelo', cos.fonteBatalha, (255,255,255), (40,210))
        if func.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - func.transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                
    #Tela de Gameover. Nessa tela toda a movimentação e interação do jogador é limitada ao jogador chegar a 0 de vida (exceto pela tecla R que reinicia o jogo).
    if cos.vidaAtual <= 0:
        janela.mudarTela('gameover')
        tocouGameOver = False
        while janela.telaAtual == 'gameover':
            if not tocouGameOver:
                pygame.mixer.music.fadeout(280)
                gameoverMusica = pygame.mixer.music.load('assets/sounds/gameovertheme.mp3')
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play(-1)
                tocouGameOver = True
                janela.atualizaTela()
            
            janela.corFundo()
            janela.tela.blit(cos.gameoverImg, (40,80))
            
            janela.escreveTexto('Pressione R para reiniciar', cos.fonte, (255,255,255), (50, 400))
            janela.atualizaTela()
                   
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    print("fechando o jogo")
                    pygame.quit()
                    exit()
                elif evento.type == KEYDOWN:
                    if evento.key == K_r:
                        func.reiniciarJogo()
            
    janela.atualizaTela() 
