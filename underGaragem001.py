import pygame
from pygame.locals import *
from modulos.alma import alma
from modulos.alma import wilson_sprite
from modulos.janelas import *
from modulos.selecoes import *
from modulos.item import *
import modulos.ataques as atk
import modulos.funcoes as func
import modulos.constantes as cos
import modulos.acoes as act
from sys import exit


while True:
    cos.fps.tick((60))
    pygame.display.update()
    eventos = pygame.event.get()
    confirmaAtaque = None

    
    for evento in eventos:
        #detecta se o tipo do evento é quando o jogador pressiona e solta rapidamente uma tecla
        if evento.type == KEYDOWN:
            if evento.key == K_j: #debug de mudar o estado das almas
                alma.trocaestado('+')
                print("trocando estado")
                if alma.estado >= len(alma.sprites):
                    alma.estado = 0
            elif evento.key == K_p: #debug de passar as rodadas
                cos.fase_atual += 1
                cos.dialogo_atual += 1
                    
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
                if cos.usouVasculhar < 3:
                    if alma.rect.colliderect(act.acoes[0].colisao):
                        cos.x += 200
                else:
                    if alma.rect.colliderect(act.acoes[0].colisao) or alma.rect.colliderect(act.acoes[1].colisao):
                        cos.x += 200
            if evento.key == K_LEFT:
                if cos.usouVasculhar < 3:
                    if alma.rect.colliderect(act.acoes[3].colisao):
                        cos.x -= 200
                else:
                    if alma.rect.colliderect(act.acoes[3].colisao) or alma.rect.colliderect(act.acoes[4].colisao):
                        cos.x -= 200
            if evento.key == K_DOWN:
                if cos.usouVasculhar < 3:
                    if alma.rect.colliderect(act.acoes[0].colisao) or alma.rect.colliderect(act.acoes[1].colisao):
                        cos.y += 35
                else:
                    if alma.rect.colliderect(act.acoes[0].colisao) or alma.rect.colliderect(act.acoes[1].colisao) or alma.rect.colliderect(act.acoes[3].colisao):
                        cos.y += 35
            if evento.key == K_UP:
                if cos.usouVasculhar < 3:
                    if alma.rect.colliderect(act.acoes[2].colisao) or alma.rect.colliderect(act.acoes[1].colisao):
                        cos.y -= 35
                else:
                    if alma.rect.colliderect(act.acoes[2].colisao) or alma.rect.colliderect(act.acoes[1].colisao) or alma.rect.colliderect(act.acoes[4].colisao):
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
                cos.mostraTransicao = True
                func.transicaoTempo = pygame.time.get_ticks()
                
        if evento.type == KEYDOWN and janela.telaAtual == 'transiçãoPoupou':
            if evento.key == K_z:
                cos.mostraTransicao = True
                func.transicaoTempo = pygame.time.get_ticks()
                
        if evento.type == KEYDOWN and janela.telaAtual == 'Créditos':
            if evento.key == K_x:
                janela.mudarTela('Menu')
            
        if evento.type == KEYDOWN and janela.telaAtual == 'FimdaPacifista':
            if evento.key == K_r:
                func.reiniciarJogo()
                janela.mudarTela('Menu')
                
        if evento.type == QUIT:
            pygame.quit()
            exit()
               
        for botao in botoes:      
            if evento.type == cos.fim_do_ataque and janela.telaAtual == 'lutaAcontecendo':#Encerra o turno de ataque inimigo
                ataque.mostrar = True
                cos.ataque_iniciou = False
                janela.mudarTela('seleções')
                cos.x = 65
                cos.y = 450
                #print("fim do ataque")
                botao.impedeTravaPos = False
                botao.comecaBatalha = False
                
                if cos.fase_atual + 1 >= len(atk.fases):
                    func.reseta_rodada(fase)
                    cos.fase_atual = randint(0, 12)
                    cos.ataques_acabaram = True
                else:
                    cos.fase_atual += 1  
                if cos.dialogo_atual + 1 >= len(cos.dialogos):
                    cos.dialogo_atual = 0
                else:
                    cos.dialogo_atual += 1
                if cos.efeito100limite:
                    cos.vidaAtual = cos.vidaAntes100limite
                    cos.vidaAntes100limite = None
                    cos.efeito100limite = False
                if cos.efeitoVerde:
                    cos.efeitoVerde = False
                if cos.consumiuItem:
                    cos.consumiuItem = False
        #eventos de combate
        if evento.type == cos.fimInv:
            alma.acertavel = True
            #print("Iframe off")

        if evento.type == KEYDOWN:
            if evento.key == K_UP and alma.estado == 1:
                cos.velocidade_azul = 0
                #print("velocidade da alma azul zerada!")
    
    #Tela de Menu
    while janela.telaAtual == 'Menu':
        if not cos.tocouMenu:
            cos.musicaFundo = pygame.mixer.music.load("assets/sounds/[Tremba's Contract].mp3")
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
            cos.tocouMenu = True
            janela.atualizaTela()
        
        janela.corFundo()
        janela.escreveTexto('UNDERGARAGEM', cos.fonte, (255,255,255), (janela.tela.get_width()/2 - 100, 100))
        pygame.draw.rect(janela.tela, 'white', cos.botaoIniciar, width=2)
        pygame.draw.rect(janela.tela, 'white', cos.botaoCreditos, width=2)
        janela.escreveTexto('Iniciar', cos.fonteCustomizada, 'white', (300,253))
        janela.escreveTexto('Créditos', cos.fonteCustomizada, 'white', (298, 298))
        alma.update()
        janela.tela.blit(alma.image, alma.rect)
        janela.atualizaTela()
                   
        for evento in pygame.event.get():
            if evento.type == QUIT:
                print("fechando o jogo")
                pygame.quit()
                exit()
            if evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    cos.y += 45
                    passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                    passaAcao.set_volume(0.3)
                    passaAcao.play()
                if evento.key == K_UP:
                    cos.y -= 45
                    passaAcao = pygame.mixer.Sound('assets/sounds/snd_squeak.mp3')
                    passaAcao.set_volume(0.3)
                    passaAcao.play()
                if evento.key == K_z:
                    if alma.rect.colliderect(cos.botaoIniciar):
                        print('pog')
                        func.iniciaJogo()
                        cos.zerouJogo = False
                    if alma.rect.colliderect(cos.botaoCreditos):
                        print('gop')
                        janela.mudarTela('Créditos')      
    #Tela de seleções    
    janela.corFundo()

    '''    
    while cos.telainicial:
            janela.corFundo()
            janela.escreveTexto('Bem vindo ao undergaragem, aperte qualquer tecla para iniciar o jogo', cos.fonteCustomizada, 'white', (janela.tela.get_width()/2, janela.tela.get_height()/2))
            for evento in eventos:
                if evento.type == KEYDOWN:
                    cos.telainicial = False
    '''
    
    janela.tela.blit(wilson_sprite.image, wilson_sprite.rect)


    func.mostrarDano()
    janela.escreveTexto(f'HP:{cos.vidaAtual}/{cos.vida}', cos.fonte, (255,255,255),(200,385))
    janela.escreveTexto('Lutar', cos.fonteCustomizada, botoes[0].cor, (85, 433))
    janela.escreveTexto('Agir', cos.fonteCustomizada, botoes[1].cor, (238, 433))
    janela.escreveTexto('Item', cos.fonteCustomizada, botoes[2].cor, (373, 433))
    janela.escreveTexto('Poupar', cos.fonteCustomizada, botoes[3].cor, (495, 433))
    
    #textos
    dialogo_atual = cos.dialogos[cos.dialogo_atual]
    if janela.telaAtual == 'seleções' and not botao.mirando:
        '''        if cos.fase_atual == 2:
        janela.escreveTexto('o próximo ataque utiliza uma mecanica diferente', cos.fonteCustomizada, 'white', (20, (janela.tela.get_height()/2)))
        janela.escreveTexto('use as setinhas para se defender', cos.fonteCustomizada, 'white', (20, (janela.tela.get_height()/2+40)))
        if cos.fase_atual == len(atk.fases):
            janela.escreveTexto('a demo acaba aqui! aja denovo para crachar o jogo :D', cos.fonteCustomizada, 'white', (20, (janela.tela.get_height()/2)))
        '''
    
        if isinstance(dialogo_atual, tuple):
            for i, linha in enumerate(dialogo_atual):
                janela.escreveTexto(linha, cos.fonteCustomizada, 'white', (20, (janela.tela.get_height()/2-40+i*20)))

        else:
            janela.escreveTexto(cos.dialogos[cos.dialogo_atual], cos.fonteCustomizada, 'white', (20, (janela.tela.get_height()/2-20)))        
    
    #vida em barra
    vida_max_barra = pygame.draw.rect(janela.tela, 'red', (330,395, (1*cos.vida), 20))
    vida_atual_barra = pygame.draw.rect(janela.tela, 'green', (330,395, (1*cos.vidaAtual), 20))

    #Desenha as Caixas
    if janela.telaAtual == 'lutaAcontecendo' or janela.telaAtual == 'inventário':
        janela.desenhaCaixa(cos.caixa_combate)
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
            cos.y += 2
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
            velocidade = 2.0
        if teclas[pygame.K_RIGHT] and not alma.rect.colliderect(colisoes[3].rect):
            cos.x += 1 * velocidade
            cos.direcao = 'direita'
        if teclas[pygame.K_LEFT] and not alma.rect.colliderect(colisoes[1].rect):
            cos.x -= 1  * velocidade
            cos.direcao = 'esquerda'
        if teclas[pygame.K_UP] and not alma.rect.colliderect(colisoes[0].rect):
            if alma.estado == 1:
                cos.y -= 1*cos.velocidade_azul
                if cos.velocidade_azul >= 0 :
                    cos.velocidade_azul -= 0.1
                    #print(cos.velocidade_azul)
            else:
                cos.y -= 1 * velocidade
            cos.direcao = 'cima'
        if teclas[pygame.K_DOWN] and not alma.rect.colliderect(colisoes[2].rect):
            cos.y += 1 * velocidade
            cos.direcao = 'baixo'

        #checks especificos de outras almas
        if alma.rect.colliderect(colisoes[2].rect) and alma.estado == 1:
            cos.y -= 2
            cos.velocidade_azul = 6.0

        '''if cos.ataques_acabaram:
            fase = atk.fases[cos.fase_atual]
        else:
            fase = atk.fases[cos.fase_atual]#declara a fase atual'''
        fase = atk.fases[cos.fase_atual]
        if not cos.ataque_iniciou: #criado para os temporizados funcionarem de maneira apropriada
            pygame.time.set_timer(cos.fim_do_ataque, fase.duracao)
            for ataque in fase.ataques:
                ataque.iniciar()
            if not cos.efeitoVerde:
                alma.trocaestado(fase.mudaalma)#muda o estado da alma para o declarado como argumento da função gerarataques
            cos.ataque_iniciou = True
            #print("Todos os ataques foram iniciados")

        for ataque in fase.ataques: #gera os ataques baseado na rodada
            resultado = ataque.atualizar(alma, func.escudo, alma.estado)
            #print("ataque atualizar foi chamado")
            if ataque.mostrar:
                ataque.draw(janela.tela)
            if resultado == "dano" and not ataque.mostrar:
                cos.vidaAtual -= (cos.wilson_atk - cos.jogador_def)
                cos.dano_snd.set_volume(0.3)
                cos.dano_snd.play()
                alma.iframe()
                #print('deu dano')
            elif resultado == "parry" and not ataque.mostrar:
                cos.parry_snd.set_volume(0.3)
                cos.parry_snd.play()
                #print('deu parry')          
            
    #Tela de seleções
    if janela.telaAtual == 'seleções':
        cos.efeito100limite = False

    #Tela de Agir
    if janela.telaAtual == 'ações':   
        func.printaAcoes()
        for acao in act.acoes:
            acao.checaAlma()
                
    #Na tela de ações,            
     if janela.telaAtual == 'transiçãoAções':
        acao = cos.acaoSelecionada
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
            elif cos.usouConversar == 4:
                textoEfeito = 'Wilson Tremba parece amigável agora'
                texto2 = ''
            elif cos.usouConversar == 5:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
            elif cos.usouConversar == 6:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
            elif cos.usouConversar == 7:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
            elif cos.usouConversar == 8:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
            elif cos.usouConversar == 9:
                textoEfeito = 'Wilson Tremba está gesticulando com suas mãos'
                texto2 = ''
                
        elif acao.nome == 'Vasculhar':
            if cos.usouVasculhar == 1:
                textoEfeito = 'Você olha ao seu redor em busca de algo...'
                texto2 = 'Você encontrou o BiGARAGEM'
                if not cos.encontrouBigaragem:
                    itens.append(Item('BiGaragem','Você recupera 50 de vida'))
                    cos.encontrouBigaragem = True
            elif cos.usouVasculhar == 2:
                textoEfeito = 'Você achou o MacLanche Infeliz.'
                texto2 = 'O Wilson Tremba parece feliz agora'
                if not cos.encontrouMc:
                    itens.append(Item('MacLanche Infeliz','De repente, tudo parece uma desgraça. + DEF, +ATK'))
                    cos.encontrouMc = True
            elif cos.usouVasculhar == 3:
                textoEfeito  = 'Você achou um REVOLVER???'
                texto2 = 'Revolver adicionado em AGIR'
                if not cos.encontrouRevolver:
                    act.acoes.append(act.Acao('O revolver que matou "Felipe"', ''))
                    cos.encontrouRevolver = True
                    cos.jogador_atk += 998      
        elif acao.nome == 'Checar':
            textoEfeito = acao.efeito
            texto2 = ''
        elif acao.nome == 'Implorar por Piedade':
            textoEfeito = acao.efeito
            texto2 = ''
        elif acao.nome == 'O revolver que matou "Felipe"':
            textoEfeito = 'Você equipou essa coisa, você escuta gritos ao seu redor'
            texto2 = 'Nele está cravado em vermelho "Felipe"'
            
        janela.escreveTexto(textoEfeito, cos.fonteBatalha, (255,255,255), (50,220))  
        janela.escreveTexto(texto2, cos.fonteBatalha, (255,255,255), (50,250))
              
        if cos.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - cos.transicaoTempo > 2000:
                cos.mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                        
    #Tela de Inventário
    if janela.telaAtual == 'inventário':
        func.printaItens(botoes)
        for item in itens:
            item.checaAlma()
            
    if janela.telaAtual == 'transiçãoItens':
        janela.escreveTexto(f'Você usou {func.itemSelecionado.nome}', cos.fonteBatalha, (255,255,255), (20,230))
        janela.escreveTexto(f'{func.itemSelecionado.descricao}', cos.fonteBatalha, (255,255,255), (20,260)) 
         
        if not cos.consumiuItem:
            func.itemSelecionado.usar()
            cos.consumiuItem = True
        if cos.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - cos.transicaoTempo > 2000:
                cos.mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                print("transição")
    
    #Tela de Piedade
    if janela.telaAtual == 'piedade':
        janela.escreveTexto('Mas não estava amarelo', cos.fonteBatalha, (255,255,255), (20,210))
        if cos.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - func.transicaoTempo > 2000:
                mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                
    if janela.telaAtual == 'transiçãoPoupou':
        janela.escreveTexto('Você poupou Wilsom Tremba', cos.fonteBatalha, 'gray', (40,210))
        if cos.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - cos.transicaoTempo > 3000:
                cos.mostraTransicao = False
                janela.mudarTela('FimdaPacifista')
                
    if janela.telaAtual == 'transiçãoMira':
        if cos.mostraTransicao:
            tempoAtual = pygame.time.get_ticks()
            if tempoAtual - cos.transicaoTempo > 1500:
                cos.mostraTransicao = False
                botoes[0].comecaBatalha = True
                cos.ataque_iniciou = False
                
    if janela.telaAtual == 'Créditos':
        janela.corFundo()
        janela.escreveTexto('Lucas Leandro', cos.fonteCustomizada, (255,255,255), (250, 150))
        janela.escreveTexto('Ronaldo Cesar', cos.fonteCustomizada, (255,255,255), (250, 200))
        janela.escreveTexto('Heitor Higino', cos.fonteCustomizada, (255,255,255), (250, 250))
        janela.escreveTexto('José Marcus', cos.fonteCustomizada, (255,255,255), (250, 300))
                
    #Tela de Gameover. Nessa tela toda a movimentação e interação do jogador é limitada ao jogador chegar a 0 de vida (exceto pela tecla R que reinicia o jogo).
    if cos.vidaAtual <= 0:
        janela.mudarTela('gameover')
        tocouGameOver = False
        while janela.telaAtual == 'gameover':
            if not tocouGameOver:
                pygame.mixer.music.fadeout(280)
                cos.musicaFundo = pygame.mixer.music.load('assets/sounds/gameovertheme.mp3')
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
    
    if cos.wilson_vida_atual <= 0:
        janela.mudarTela('FimdaGenocida')
        tocouGenocida = False
        while janela.telaAtual == 'FimdaGenocida':
            if not tocouGenocida:
                cos.musicaFundo = pygame.mixer.music.load("assets/sounds/[Tremba's Contract].mp3")
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play(-1)
                tocouGenocida = True
                janela.atualizaTela()
            
            janela.corFundo()
            janela.escreveTexto('Você tentou matar o Wilson Tremba....', cos.fonteCustomizada, (255,255,255), (46, 150))
            janela.escreveTexto('Mas ele não pode ser morto.', cos.fonteCustomizada, (255,255,255), (56, 250))
            janela.escreveTexto('Aperte R para reiniciar o jogo', cos.fonteCustomizada, (255,255,255), (26, 400))
            janela.atualizaTela()
            cos.wilson_vida_atual = 1
            
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    print("fechando o jogo")
                    pygame.quit()
                    exit()
                elif evento.type == KEYDOWN:
                    if evento.key == K_r:
                        cos.zerouJogo = True
                        func.reiniciarJogo()
                        janela.mudarTela('Menu')
                        cos.x = 286
                        cos.y = 270
                        
    while janela.telaAtual == 'FimdaPacifista':
        if not cos.tocouFimPacifista:
            cos.musicaFundo = pygame.mixer.music.load("assets/sounds/[Tremba's Contract].mp3")
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
            cos.tocouFimPacifista = True
            janela.atualizaTela()
        janela.corFundo()
        janela.escreveTexto('Você terminou o Jogo! Parabéns!', cos.fonteCustomizada, (255,255,255), (158, 150))
        janela.escreveTexto('Se quiser entrar no nosso Hall da Fama mande um email', cos.fonteCustomizada, (255,255,255), (55, 200))
        janela.escreveTexto('para esse endereço agaragemdoperigo@gmail.com', cos.fonteCustomizada, (255,255,255), (78, 250))
        janela.escreveTexto('Aperte R para reiniciar o jogo', cos.fonteCustomizada, (255,255,255), (26, 400))
        janela.atualizaTela()
        
        for evento in pygame.event.get():
                if evento.type == QUIT:
                    print("fechando o jogo")
                    pygame.quit()
                    exit()
                elif evento.type == KEYDOWN:
                    if evento.key == K_r:
                        cos.zerouJogo = True
                        func.reiniciarJogo()
                        janela.mudarTela('Menu')
                        cos.x = 286
                        cos.y = 270
            
    janela.atualizaTela()
